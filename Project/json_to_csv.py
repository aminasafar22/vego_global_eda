import pandas as pd
df = pd.read_json("./DATA/customers.json")

df.to_csv("./DATA/customers.csv", index=False)
print(df.head())
 