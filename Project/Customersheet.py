import pandas as pd

df = pd.read_csv("./Prpject/customers.csv")
df = df.drop(columns=["Suffix", "Title", "AddressLine2", "NameStyle", "SpanishEducation", "SpanishOccupation", "FrenchEducation", "FrenchOccupation"])
print(df.isnull().sum())
df["MiddleName"] = df["MiddleName"].fillna("No middle name")
print(df.dtypes)
df = df.astype({
    "DateFirstPurchase": "datetime64[ns]",
    "BirthDate": "datetime64[ns]",
    "Gender": "category",
    "MaritalStatus": "category",
})

print(df.isnull().sum())
print(df.dtypes)

df.to_csv("Customers details.csv", index=False)
