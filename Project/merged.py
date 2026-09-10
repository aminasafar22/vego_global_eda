import pandas as pd

sales = pd.read_csv(r"/home/bouchra/mina/Project/Sales details.csv")
customers = pd.read_csv(r"/home/bouchra/mina/Project/Customers details.csv")
products = pd.read_csv(r"/home/bouchra/mina/Project/Product catalog details.csv")
geography = pd.read_csv(r"/home/bouchra/mina/Project/Geography details.csv")

geography = geography.drop(columns=["index"], errors="ignore")

merged = pd.merge(
    sales,
    customers,
    on="CustomerKey",
    how="left",
    suffixes=("", "_customer"),
)

merged = pd.merge(
    merged,
    products,
    on="ProductKey",
    how="left",
    suffixes=("", "_product"),
)

merged = pd.merge(
    merged,
    geography,
    on="SalesTerritoryKey",
    how="left",
    suffixes=("", "_geo"),
)

#check
print("Sales rows:            ", len(sales))
print("Merged rows:           ", len(merged))          
print("Merged columns:        ", merged.shape[1])
print("Any missing customer?  ", merged["FirstName"].isna().sum())
print("Any missing product?   ", merged["EnglishProductName"].isna().sum())
print("Any missing geography? ", merged["SalesTerritoryRegion"].isna().sum())

merged = merged.astype({
    "OrderDate": "datetime64[ns]",
    "ShipDate": "datetime64[ns]",
    "BirthDate": "datetime64[ns]",
    "DateFirstPurchase": "datetime64[ns]",
    "DaysToManufacture": "timedelta64[ns]",
    "StartDate": "datetime64[ns]",
    "Gender": "category",
    "MaritalStatus": "category",
    "FinishedGoodsFlag": "bool",
    "HouseOwnerFlag": "bool",
})
print(merged.info())

merged.to_csv("./Project/Unified_Sales_Data.csv", index=False)