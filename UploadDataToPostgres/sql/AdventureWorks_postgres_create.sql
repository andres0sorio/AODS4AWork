CREATE TABLE "Product" (
	"ProductID" serial ,
	"Name" character varying(50) ,
	"ProductNumber" character varying(25) ,
	"MakeFlag" char(5) ,
	"FinishedGoodsFlag" char(5) ,
	"Color" character varying(15) ,
	"SafetyStockLevel" smallint ,
	"ReorderPoint" smallint ,
	"StandardCost" money ,
	"ListPrice" money ,
	"Size" character varying(5) ,
	"SizeUnitMeasureCode" char(3) ,
	"WeightUnitMeasureCode" char(3) ,
	"Weight" DECIMAL ,
	"DaysToManufacture" int ,
	"ProductLine" char(2) ,
	"Class" char(2) ,
	"Style" char(2) ,
	"ProductSubcategoryID" int ,
	"ProductModelID" int ,
	"SellStartDate" DATE ,
	"SellEndDate" DATE ,
	"DiscontinuedDate" DATE ,
	"rowguid" uuid ,
	"ModifiedDate" DATE ,
	CONSTRAINT "Product_pk" PRIMARY KEY ("ProductID")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "SalesPerson" (
	"BusinessEntityID" serial ,
	"TerritoryID" int ,
	"SalesQuota" money ,
	"Bonus" money ,
	"CommissionPct" money ,
	"SalesYTD" money ,
	"SalesLastYear" money ,
	"rowguid" uuid ,
	"ModifiedDate" DATE ,
	CONSTRAINT "SalesPerson_pk" PRIMARY KEY ("BusinessEntityID")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "ProductReview" (
	"ProductReviewID" int ,
	"ProductID" int ,
	"ReviewerName" varchar(50) ,
	"ReviewDate" DATE ,
	"EmailAddress" varchar(50) ,
	"Rating" int ,
	"Comments" varchar(3850) ,
	"ModifiedDate" DATE ,
	CONSTRAINT "ProductReview_pk" PRIMARY KEY ("ProductReviewID")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "ProductModelProductDescriptionCulture" (
	"ProductModelID" int ,
	"ProductDescriptionID" int ,
	"CultureID" int ,
	"ModifiedDate" DATE ,
	CONSTRAINT "ProductModelProductDescriptionCulture_pk" PRIMARY KEY ("ProductModelID","ProductDescriptionID","CultureID")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "ProductDescription" (
	"ProductDescriptionID" int ,
	"Description" varchar(400) ,
	"rowguid" uuid ,
	"ModifiedDate" DATE ,
	CONSTRAINT "ProductDescription_pk" PRIMARY KEY ("ProductDescriptionID")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "ProductCategory" (
	"ProductCategoryID" int ,
	"Name" varchar(50) ,
	"rowguid" uuid ,
	"ModifiedDate" DATE ,
	CONSTRAINT "ProductCategory_pk" PRIMARY KEY ("ProductCategoryID")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "ProductSubCategory" (
	"ProductSubcategoryID" int ,
	"ProductCategoryID" int ,
	"Name" varchar(50) ,
	"rowguid" uuid ,
	"ModifiedDate" DATE ,
	CONSTRAINT "ProductSubCategory_pk" PRIMARY KEY ("ProductSubcategoryID")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "SalesOrderHeader" (
	"SalesOrderID" int ,
	"RevisionNumber" int ,
	"OrderDate" DATE ,
	"DueDate" DATE ,
	"ShipDate" DATE ,
	"Status" int ,
	"OnlineOrderFlag" char(5) ,
	"PurchaseOrderNumber" varchar(25) ,
	"AccountNumber" varchar(25) ,
	"CustomerID" int ,
	"SalesPersonID" int ,
	"TerritoryID" int ,
	"BillToAddressID" int ,
	"ShipToAddressID" int ,
	"ShipMethodID" int ,
	"CreditCardID" int ,
	"CreditCardApprovalCode" varchar(5) ,
	"CurrencyRateID" int ,
	"SubTotal" money ,
	"TaxAmt" money ,
	"Freight" money ,
	"TotalDue" money ,
	"Comment" varchar(128) ,
	"rowguid" uuid ,
	"ModifiedDate" DATE ,
	CONSTRAINT "SalesOrderHeader_pk" PRIMARY KEY ("SalesOrderID")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "SalesOrderDetail" (
	"SalesOrderID" int ,
	"SalesOrderDetailID" int ,
	"CarrierTrackingNumber" varchar(25) ,
	"OrderQty" int ,
	"ProductID" int ,
	"SpecialOfferID" int ,
	"UnitPrice" money ,
	"UnitPriceDiscount" money ,
	"rowguid" uuid ,
	"ModifiedDate" DATE ,
	CONSTRAINT "SalesOrderDetail_pk" PRIMARY KEY ("SalesOrderID","SalesOrderDetailID")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "SalesTerritory" (
	"TerritoryID" int ,
	"Name" varchar(50) ,
	"CountryRegionCode" varchar(3) ,
	"Group" varchar(50) ,
	"SalesYTD" money ,
	"SalesLastYear" money ,
	"CostYTD" money ,
	"CostLastYear" money ,
	"rowguid" uuid ,
	"ModifiedDate" DATE ,
	CONSTRAINT "SalesTerritory_pk" PRIMARY KEY ("TerritoryID")
) WITH (
  OIDS=FALSE
);

CREATE TABLE "CountryRegionCurrency" (
	"CountryRegionCode" varchar(3) ,
	"CurrencyCode" char(3) ,
	"ModifiedDate" DATE ,
	CONSTRAINT "CountryRegionCurrency_pk" PRIMARY KEY ("CountryRegionCode")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "CurrencyRate" (
	"CurrencyRateID" int ,
	"CurrencyRateDate" DATE ,
	"FromCurrencyCode" char(3) ,
	"ToCurrencyCode" char(3) ,
	"AverageRate" money ,
	"EndOfDayRate" money ,
	"ModifiedDate" DATE ,
	CONSTRAINT "CurrencyRate_pk" PRIMARY KEY ("CurrencyRateID")
) WITH (
  OIDS=FALSE
);

ALTER TABLE "Product" ADD CONSTRAINT "Product_fk0" FOREIGN KEY ("ProductSubcategoryID") REFERENCES "ProductSubCategory"("ProductSubcategoryID");

ALTER TABLE "SalesPerson" ADD CONSTRAINT "SalesPerson_fk0" FOREIGN KEY ("TerritoryID") REFERENCES "SalesTerritory"("TerritoryID");

ALTER TABLE "ProductReview" ADD CONSTRAINT "ProductReview_fk0" FOREIGN KEY ("ProductID") REFERENCES "Product"("ProductID");

ALTER TABLE "ProductModelProductDescriptionCulture" ADD CONSTRAINT "ProductModelProductDescriptionCulture_fk0" FOREIGN KEY ("ProductDescriptionID") REFERENCES "ProductDescription"("ProductDescriptionID");

ALTER TABLE "ProductSubCategory" ADD CONSTRAINT "ProductSubCategory_fk0" FOREIGN KEY ("ProductCategoryID") REFERENCES "ProductCategory"("ProductCategoryID");

ALTER TABLE "SalesOrderHeader" ADD CONSTRAINT "SalesOrderHeader_fk0" FOREIGN KEY ("SalesPersonID") REFERENCES "SalesPerson"("BusinessEntityID");
ALTER TABLE "SalesOrderHeader" ADD CONSTRAINT "SalesOrderHeader_fk1" FOREIGN KEY ("TerritoryID") REFERENCES "SalesTerritory"("TerritoryID");

ALTER TABLE "SalesOrderDetail" ADD CONSTRAINT "SalesOrderDetail_fk0" FOREIGN KEY ("SalesOrderID") REFERENCES "SalesOrderHeader"("SalesOrderID");
ALTER TABLE "SalesOrderDetail" ADD CONSTRAINT "SalesOrderDetail_fk1" FOREIGN KEY ("ProductID") REFERENCES "Product"("ProductID");


