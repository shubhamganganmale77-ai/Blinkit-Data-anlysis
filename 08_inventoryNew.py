import pandas as pd
df8=pd.read_csv("blinkit_inventoryNew.csv")
duplicate=df8.duplicated(subset="product_id")#no remove repetaing product id because it represent inventory for different days
negative_stock=df8["stock_received"]<0
# print(zero_stock.value_counts())#no zero or less than zero values
negative_damaged=df8["stock_received"]<0
# print(negative_damaged.sum())#No negative damaged and negative stock
df8["date"]=pd.to_datetime(df8["date"],errors="coerce")
# print(df8.isnull().sum())
#data is cleaned.
df8.to_csv("cleaned_inventoryNew.csv",index=False)