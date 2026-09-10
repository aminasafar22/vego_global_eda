import pandas as pd
df = pd.read_csv("./Prpject/table11.csv")
print(df.head(11))
df = df.drop(columns=["SalesTerritoryAlternateKey"])
df.to_csv("Geography details.csv", index=False)

