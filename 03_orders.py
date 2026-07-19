import pandas as pd 
df3=pd.read_csv("blinkit_orders.csv")
# print(df3.isnull().sum())
# print(df3.duplicated(subset="order_id").value_counts())
df3["order_date"]=pd.to_datetime(df3["order_date"],errors="coerce")
df3["promised_delivery_time"]=pd.to_datetime(df3["promised_delivery_time"],errors="coerce")
df3["actual_delivery_time"]=pd.to_datetime(df3["actual_delivery_time"],errors="coerce")
# print(df3["promised_delivery_time"].isnull().value_counts())
# print(df3["actual_delivery_time"].isnull().value_counts())
df3=df3[df3["order_total"]>0]
Q1=df3["order_total"].quantile(0.25)
Q3=df3["order_total"].quantile(0.75)
IQR=Q3-Q1
lower=Q1-1.5*IQR
upper=Q3+1.5*IQR
Outliers=df3[(df3["order_total"]<lower ) | (df3["order_total"]>upper)]
# print(Outliers)#Outliers detected but they are real and accptable

# Analysis
# 1)Total revenue
total_revenue=df3["order_total"].sum()
print("total Revenue is:",total_revenue,"(in rupees)")
# 2)Average order value
avg_order_val=df3["order_total"].mean()
print("The average order value is:",avg_order_val)
# 3)Payment method distribution
payment_method_distribution=df3["payment_method"].value_counts()
print("Payment method distribution is:\n",payment_method_distribution)
# 4)Orders by delivery status
orders_by_delivery_status=df3["delivery_status"].value_counts()
print("Delivery_status:",orders_by_delivery_status)
# 5)Orders per day
orders_per_day=df3["order_date"].dt.date.value_counts().sort_index()
print("Orders per day are:\n",orders_per_day)
df3.to_csv("cleaned_orders.csv",index=False)

print(df3.info())