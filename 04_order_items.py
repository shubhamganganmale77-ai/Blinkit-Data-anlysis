import pandas as pd
df4=pd.read_csv("blinkit_order_items.csv")
# print(df4.duplicated(subset="order_id").value_counts())
# print(df4.isnull().sum())
df4=df4[df4["quantity"]>0]
df4=df4[df4["unit_price"]>0]
Q1=df4["unit_price"].quantile(0.25)
Q3=df4["unit_price"].quantile(0.75)
IQR=Q3-Q1
lower=Q1-1.5*IQR
upper=Q3+1.5*IQR
Outliers=df4[(df4["unit_price"]<lower ) | (df4["unit_price"]>upper)]
# print(Outliers)#No outlier detected
df4.to_csv("cleaned_order_items.csv",index=False)