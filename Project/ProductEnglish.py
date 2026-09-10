import pandas as pd

df = pd.read_csv("./Prpject/EnglishProduct.csv")

print(df.info())
df.drop_duplicates(inplace=True)
df = df.drop(columns=["SpanishProductName", "FrenchProductName", "ProductSubcategoryKey", "WeightUnitMeasureCode", "SizeUnitMeasureCode", "SizeRange", "Weight", "Style", "EndDate", "EnglishDescription", "HebrewDescription", "ArabicDescription", "ThaiDescription", "GermanDescription", "FrenchDescription", "ChineseDescription", "TurkishDescription", "JapaneseDescription"])
print(df.head())

df["Status"] = df["Status"].fillna("Current")
print(df.drop_duplicates())

print(df["Size"].value_counts())
df["Size"] = df["Size"].fillna("Standerdized")
df["Size"] = df["Size"].replace("L", 38).replace("M", 36).replace("S", 34).replace("XL", 40)
print(df["Size"].value_counts())

df = df.astype({
    "StartDate": "datetime64[ns]",
    "FinishedGoodsFlag": "bool",
})
print(df.dtypes)
df = df.dropna(subset=["DealerPrice", "ListPrice", "ProductAlternateKey", "EnglishProductName"])
df["StandardCost"] = df["StandardCost"].fillna(df["StandardCost"].mean())
print(df.isnull().sum())

print(df["ProductAlternateKey"].unique())
print(df["EnglishProductName"].unique())

df["Color"] = df["Color"].fillna("Not Specified")
df["Class"] = df["Class"].fillna("Not Specified")
df["ProductLine"] = df["ProductLine"].fillna("Not Specified")
print(df.isnull().sum())

df.to_csv("Product catalog details.csv", index=False)