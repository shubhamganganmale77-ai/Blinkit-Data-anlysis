import pandas as pd
df7=pd.read_csv("blinkit_inventory.csv")
duplicate=df7.duplicated(subset="product_id")#no remove repetaing product id because it represent inventory for different days
negative_stock=df7["stock_received"]<0
# print(zero_stock.value_counts())#no zero or less than zero values
negative_damaged=df7["stock_received"]<0
# print(negative_damaged.sum())#No negative damaged negative stock
df7["date"]=pd.to_datetime(df7["date"],dayfirst=True,errors="coerce")
# print(df7.isnull().sum())

# Analysis
# 1)Total stock recieved
stock_recieved=df7["stock_received"].sum()
print("Total stock recieved:",stock_recieved)
# 2)Total damaged stock
stock_damaged=df7["damaged_stock"].sum()
print("Total damaged stock",stock_damaged)
# 3)Monthly stock recieved
df7["month"]=df7["date"].dt.month_name()
monthly_stock=df7.groupby("month")["stock_received"].sum()
print(monthly_stock)
df7.to_csv("cleaned_inventory.csv",index=False)
