library(INLA)
library(openxlsx)
library(raster)
library(mapview)
#setwd("Downloads/datosproyecto")

modeloaccidentes<-function(fecha,hora){
  fecha1<-as.Date(fecha)
  HoraDecimal <- function(x){
    sum(unlist(lapply(strsplit(x, split=":"), as.numeric)) * c(1, 1/60, 1/3600))/24
  }
  datos<-read.xlsx("datosproyecto/base.xlsx",sheet = 1)
  datos1<-SpatialPointsDataFrame(coords=cbind(datos$Longitud,datos$Latitud),data=datos[,c("Fecha.accidente","Hora.recibo.llamada")],
                                 proj4string=CRS("+init=epsg:4326 +proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs +towgs84=0,0,0"))
  crs_new <- "+proj=tmerc +lat_0=4.59620041666667 +lon_0=-74.0775079166667
+k=1 +x_0=1000000 +y_0=1000000 +ellps=GRS80
+towgs84=0,0,0,0,0,0,0 +units=m +no_defs"
  datos1new <- spTransform(datos1,crs_new)
  
  datos1new$Fecha.accidente <- as.character(datos1new$Fecha.accidente)
  idxcorr <- which(!is.na(sapply(datos1new$Fecha.accidente,as.numeric))) ##Para corregir ##
  fechas0 <- as.Date(as.numeric(datos1new$Fecha.accidente[idxcorr]),origin="1899-12-30")
  fechas1 <- sapply(fechas0,function(x){
    ano <- substr(x,1,4)
    dia <-substr(x,6,7)
    mes <- substr(x,9,10)
    fechanew <- paste(dia,mes,ano,sep="/")
    return(fechanew)
  })
  datos1new$Fecha.accidente[idxcorr] <- fechas1
  datos1new$Fecha.accidente<- as.Date(datos1new$Fecha.accidente,format="%d/%m/%Y")
  datos1new$Fecha.accidente-min(datos1new$Fecha.accidente)
  fechamax<-max(datos1new$Fecha.accidente)
  fechamin<-min(datos1new$Fecha.accidente)
  tiempo <- as.numeric(datos1new$Fecha.accidente-min(datos1new$Fecha.accidente))
  datos1new$dias <- tiempo
  datos1new$t <- datos1new$Hora.recibo.llamada + datos1new$dias
  datos1new <- datos1new[,c("t")]
  
  dias<-as.numeric(fecha1-fechamin)
  hora<-HoraDecimal(hora)
  dias2<-dias+hora
  
  if(dias2>max(datos1new$t)){knots=c(seq(0,max(datos1new$t),length.out=10),dias2); pos=11} 
  else{knots0=seq(0,max(datos1new$t),length.out=10); pos0=length(which(knots0<dias2)); knots=c(knots0[1:pos0],dias2,knots0[(pos0+1):length(knots0)]);pos=pos0+1}
  
  
modeloaccidentes1 <- function(knots,pos){
  
  
  hist(datos1new$t,breaks=100)
  
  n <- nrow(datos1new)
  k <- length(knots)
  if(is.null(knots)){tknots <- seq(min(datos1new$t), max(datos1new$t), length = k)}
  else{tknots <- knots}
  mesh.t <- inla.mesh.1d(tknots)
  
  carretera<-shapefile("datosproyecto/Buffer_50mViaNeivaGirardot.shp")
  
  
  mesh.s <- inla.mesh.2d(datos1new,
                         boundary = inla.sp2segment(carretera),
                         max.edge = c(5000, 10000),offset =c(100,-0.1),cutoff=1000) # a crude mesh
  mesh.s$n
  spde <- inla.spde2.pcmatern(mesh = mesh.s,
                              prior.range = c(5, 0.01), # P(practic.range < 5) = 0.01
                              prior.sigma = c(1, 0.01)) # P(sigma > 1) = 0.01
  m <- spde$n.spde
  
  Ast <- inla.spde.make.A(mesh = mesh.s, loc = datos1new@coords,
                          n.group = length(mesh.t$n), group = datos1new$t,
                          group.mesh = mesh.t)
  dim(Ast)
  
  idx <- inla.spde.make.index('s', spde$n.spde, n.group = mesh.t$n)
  
  ## Making the LGCP model ##
  source("spde-book-functions.R")
  dmesh <- book.mesh.dual(mesh.s)
  crs(dmesh) <- crs(carretera)
  library(rgeos)
  w <- sapply(1:length(dmesh), function(i) {
    if (gIntersects(dmesh[i,], carretera))
      return(gArea(gIntersection(dmesh[i,], carretera)))
    else return(0)
  })
  gArea(carretera)
  
  st.vol <- rep(w, k) * rep(diag(inla.mesh.fem(mesh.t)$c0), m)
  
  y <- rep(0:1, c(k * m, n))
  expected <- c(st.vol, rep(0, n))
  stk <- inla.stack(
    data = list(y = y, expect = expected),
    A = list(rbind(Diagonal(n = k * m), Ast), 1),
    effects = list(idx, list(a0 = rep(1, k * m + n))))
  
  pcrho <- list(prior = 'pc.cor1', param = c(0.7, 0.7))
  form <- y ~ 0 + a0 + f(s, model = spde, group = s.group,
                         control.group = list(model = 'ar1',
                                              hyper = list(rho = pcrho)))
  
  burk.res <- inla(form, family = 'poisson',
                   data = inla.stack.data(stk), E = expect,
                   control.predictor = list(A = inla.stack.A(stk)),
                   control.inla = list(strategy = 'adaptive'),
                   verbose=TRUE)
  
  eta.at.integration.points <- burk.res$summary.fix[1,1] +
    burk.res$summary.ran$s$mean
  c(n = n, 'E(n)' = sum(st.vol * exp(eta.at.integration.points)))
  
  carretera500 <- shapefile("datosproyecto/Buffer_500mViaNeivaGirardot.shp")
  extcarr <- extent(carretera500)
  r0 <- diff(c(extcarr[1],extcarr[2])) / diff(c(extcarr[3],extcarr[4]))
  prj.acc <- inla.mesh.projector(mesh.s, xlim = c(extcarr[1],extcarr[2]),
                                 ylim = c(extcarr[3],extcarr[4]), dims = c(1000, 1000))
  carretera.sp <- SpatialPolygons(carretera500@polygons,proj4string = crs(carretera))
  ov <- over(SpatialPoints(prj.acc$lattice$loc,proj4string = crs(carretera)), carretera.sp)
  m.prj <- lapply(1:k, function(j) {
    r <- inla.mesh.project(prj.acc,
                           burk.res$summary.ran$s$mean[1:m + (j - 1) * m])
    r[is.na(ov)] <- NA
    return(r)
  })
  
  
  igr <- apply(abs(outer(datos1new$t, mesh.t$loc, '-')), 1, which.min)
  zlm <- range(unlist(m.prj), na.rm = TRUE)
  
  library(spatstat)
  raster_list <- list()
  
  im2rast <- function(im){
    gridlocs <- expand.grid(im$xcol,im$yrow)
    cov1.sp <- SpatialPointsDataFrame(coords = gridlocs,data = data.frame(cov=c(anti_t(rotate(rotate(im$v))))))
    r <- raster(cov1.sp)
    xstp <- im$xstep
    ystp <- im$ystep
    r1<-disaggregate(r, fact=res(r)/c(xstp,ystp))
    cov1.rast <- rasterize(cov1.sp@coords,r1,cov1.sp$cov, fun=mean,na.rm=T)
  }
  
  for(j in 1:k){
    im_tmp<- im(m.prj[[j]],xcol=prj.acc$x,yrow=prj.acc$y)
    rotate <- function(x) (apply(t(x), 2, rev))
    rotate2 <- function(x) (apply(t(x), 1, rev))
    im1 <- im((rotate(im_tmp$v)),xcol=prj.acc$x,yrow=prj.acc$y)
    im2 <- im(reflect(im1)$v,xcol=prj.acc$x,yrow=prj.acc$y)
    im3 <- im(rotate2(reflect(im2)$v),xcol=prj.acc$x,yrow=prj.acc$y)
    rt <- raster(im3,crs=crs(carretera.sp))
    raster_list[[j]] <- 1-exp(-exp(rt))
  }
  oneraster <- raster_list[[pos]]
  
  return(oneraster)
  
}

newraster <- modeloaccidentes1(knots,pos)
return(newraster)
}

# fecha<-"2021-09-01"
# hora<-"12:30:00"
# salida<-modeloaccidentes(fecha,hora)

# fecha<-"2021-09-01" ---->>> ARG 1
# hora<-"12:30:00" ---->>> ARG 2
# ejecucion: Rscript myScript.R 5 100

# args <- commandArgs(trailingOnly = TRUE)

args=(commandArgs(TRUE))

if(length(args)==0){
    print("No arguments supplied.")
    ##supply default values
    a = "2021-09-01"
    b = "12:30:00"
}else{
    for(i in 1:length(args)){
         eval(parse(text=args[[i]]))
    }
}


print(a)
print(b)

salida<-modeloaccidentes(a, b)

rf <- writeRaster(salida, filename=file.path("model_output.tif"), format="GTiff", overwrite=TRUE)


