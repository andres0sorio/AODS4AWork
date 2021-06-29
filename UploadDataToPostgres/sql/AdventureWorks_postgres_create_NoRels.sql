CREATE TABLE "Product" (
    "ProductID" serial,
    "Name" character varying(50),
    "ProductNumber" character varying(25),
    "MakeFlag" char(5),
    "FinishedGoodsFlag" char(5),
    "Color" character varying(15),
    "SafetyStockLevel" smallint,
    "ReorderPoint" smallint,
    "StandardCost" money,
    "ListPrice" money,
    "Size" character varying(5),
    "SizeUnitMeasureCode" char(3),
    "WeightUnitMeasureCode" char(3),
    "Weight" DECIMAL,
    "DaysToManufacture" int,
    "ProductLine" char(2),
    "Class" char(2),
    "Style" char(2),
    "ProductSubcategoryID" int,
    "ProductModelID" int,
    "SellStartDate" DATE,
    "SellEndDate" DATE,
    "DiscontinuedDate" DATE,
    "rowguid" uuid,
    "ModifiedDate" DATE
) WITH (OIDS = FALSE);
CREATE TABLE "SalesPerson" (
    "BusinessEntityID" serial,
    "TerritoryID" int,
    "SalesQuota" money,
    "Bonus" money,
    "CommissionPct" money,
    "SalesYTD" money,
    "SalesLastYear" money,
    "rowguid" uuid,
    "ModifiedDate" DATE
) WITH (OIDS = FALSE);
CREATE TABLE "ProductReview" (
    "ProductReviewID" int,
    "ProductID" int,
    "ReviewerName" varchar(50),
    "ReviewDate" DATE,
    "EmailAddress" varchar(50),
    "Rating" int,
    "Comments" varchar(3850),
    "ModifiedDate" DATE
) WITH (OIDS = FALSE);
CREATE TABLE "ProductModelProductDescriptionCulture" (
    "ProductModelID" int,
    "ProductDescriptionID" int,
    "CultureID" varchar(15),
    "ModifiedDate" DATE
) WITH (OIDS = FALSE);
CREATE TABLE "ProductDescription" (
    "ProductDescriptionID" int,
    "Description" varchar(400),
    "rowguid" uuid,
    "ModifiedDate" DATE
) WITH (OIDS = FALSE);
CREATE TABLE "ProductCategory" (
    "ProductCategoryID" int,
    "Name" varchar(50),
    "rowguid" uuid,
    "ModifiedDate" DATE
) WITH (OIDS = FALSE);
CREATE TABLE "ProductSubCategory" (
    "ProductSubcategoryID" int,
    "ProductCategoryID" int,
    "Name" varchar(50),
    "rowguid" uuid,
    "ModifiedDate" DATE
) WITH (OIDS = FALSE);
CREATE TABLE "SalesOrderHeader" (
    "SalesOrderID" int,
    "RevisionNumber" int,
    "OrderDate" DATE,
    "DueDate" DATE,
    "ShipDate" DATE,
    "Status" int,
    "OnlineOrderFlag" char(5),
    "PurchaseOrderNumber" varchar(25),
    "AccountNumber" varchar(25),
    "CustomerID" int,
    "SalesPersonID" int,
    "TerritoryID" int,
    "BillToAddressID" int,
    "ShipToAddressID" int,
    "ShipMethodID" int,
    "CreditCardID" int,
    "CreditCardApprovalCode" varchar(15),
    "CurrencyRateID" int,
    "SubTotal" money,
    "TaxAmt" money,
    "Freight" money,
    "TotalDue" money,
    "Comment" varchar(128),
    "rowguid" uuid,
    "ModifiedDate" DATE
) WITH (OIDS = FALSE);
CREATE TABLE "SalesOrderDetail" (
    "SalesOrderID" int,
    "SalesOrderDetailID" int,
    "CarrierTrackingNumber" varchar(25),
    "OrderQty" int,
    "ProductID" int,
    "SpecialOfferID" int,
    "UnitPrice" money,
    "UnitPriceDiscount" money,
    "rowguid" uuid,
    "ModifiedDate" DATE
) WITH (OIDS = FALSE);
CREATE TABLE "SalesTerritory" (
    "TerritoryID" int,
    "Name" varchar(50),
    "CountryRegionCode" varchar(3),
    "Group" varchar(50),
    "SalesYTD" money,
    "SalesLastYear" money,
    "CostYTD" money,
    "CostLastYear" money,
    "rowguid" uuid,
    "ModifiedDate" DATE
) WITH (OIDS = FALSE);
CREATE TABLE "CountryRegionCurrency" (
    "CountryRegionCode" varchar(3),
    "CurrencyCode" char(3),
    "ModifiedDate" DATE
) WITH (OIDS = FALSE);
CREATE TABLE "CurrencyRate" (
    "CurrencyRateID" int,
    "CurrencyRateDate" DATE,
    "FromCurrencyCode" char(3),
    "ToCurrencyCode" char(3),
    "AverageRate" money,
    "EndOfDayRate" money,
    "ModifiedDate" DATE
) WITH (OIDS = FALSE);