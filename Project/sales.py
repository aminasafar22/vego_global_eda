import pandas as pd
df = pd.read_csv("./Prpject/sales.csv")

df = df.drop(columns=["RevisionNumber", "OrderQuantity", "UnitPriceDiscountPct", "DiscountAmount"])
currency_columns = ['29', '6', '98', '19', '36', '100']
print(df[currency_columns].head())
print([repr(col) for col in df.columns])
currency_columns = [col for col in df.columns 
                    if str(col) in ['29', '6', '98', '19', '36', '100']]

print(currency_columns)
currency_columns = ['29', '6', '98', '19', '36', '100']

df = df.melt(
    id_vars=[col for col in df.columns if col not in currency_columns],
    value_vars=currency_columns,
    var_name='CurrencyKey',
    value_name='SalesAmount'
)
print(df.dtypes)
print(df["SalesAmount"].unique())
currency_map = { '6' : 'AUD', '19' : 'CAD', '29' : 'DEM', '36' : 'EUR', '98' : 'GBP', '100' : 'USD'}
df["CurrencyKey"] = df["CurrencyKey"].map(currency_map)
print(df["CurrencyKey"].unique())
print(df.tail())

def fill_sales(row):
    if row['CurrencyKey'] == 'USD' and pd.isna(row['SalesAmount']):
        return row['UnitPrice']
    return row['SalesAmount']
df['SalesAmount'] = df.apply(fill_sales, axis=1)
#checking shape
print(df.loc[
    (df['SalesAmount'].isna()) & (df['CurrencyKey'] == 'GBP')
].shape[0])

for i in range(len(df)):
    if pd.isna(df.loc[i, 'SalesAmount']):
        df.loc[i, 'CurrencyKey'] = 'USD'
        df.loc[i, 'SalesAmount'] = df.loc[i, 'UnitPrice']

print(df['SalesAmount'].isna().sum())

df = df.astype({
    "OrderDate": "datetime64[ns]",
    "ShipDate": "datetime64[ns]",
})
print(df.drop_duplicates())
df.to_csv("./Project/Sales details.csv", index=False)

