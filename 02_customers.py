import pandas as pd
df2=pd.read_csv("blinkit_customers.csv")
df2=df2.drop_duplicates(subset="email")#removed duplicated emails
df2["phone"]=df2["phone"].astype("string")
df2["phone"]=df2["phone"].str.replace("+91","")
# print(df2[(df2["phone"].str.len()>10)&(df2["phone"].str.len()<10)])#Checking for invalid phone number
df2["phone"]=df2["phone"].astype("int")
df2["pincode"]=df2["pincode"].astype("str")
df2=df2[df2["pincode"].str.len()==6]
df2["pincode"]=df2["pincode"].astype("int")
# Converting registration_date into pandas data time format
df2["registration_date"]=pd.to_datetime(df2["registration_date"],errors="coerce")
df2=df2.dropna(subset="registration_date")
df2["year"]=df2["registration_date"].dt.year#year of every product 
df2["month"]=df2["registration_date"].dt.month_name()#return month of product 
#outliers in avg_order_value
Q1=df2["avg_order_value"].quantile(0.25)
Q3=df2["avg_order_value"].quantile(0.75)
IQR=Q3-Q1
lower=Q1-1.5*IQR
upper=Q3+1.5*IQR
Outliers=df2[(df2["avg_order_value"]<lower ) | (df2["avg_order_value"]>upper)]
# print(Outliers)#no outliers present

# Analysis
# 1)Top customers by total orders
top_customers=df2[["customer_name","total_orders"]]
max_order=df2["total_orders"].max()
top_customers=top_customers[top_customers["total_orders"]==max_order]
print("Customers with the highest orders are as follow:\n",top_customers.reset_index(drop=True))#106 Customers with highest order count
# 2)Customer segment distribution
Customer_distribution=df2["customer_segment"].value_counts()
print("Customer distribution as per segment:\n",Customer_distribution)
# 3)Highest average order value
max_avg_order_val=df2["avg_order_value"].max()
Highest_avg_order_val=df2[["customer_name","avg_order_value",]]
Highest_avg_order_val=Highest_avg_order_val[Highest_avg_order_val["avg_order_value"]==max_avg_order_val]
print("Highest average order values:\n",Highest_avg_order_val.reset_index(drop=True))
df2.to_csv("cleaned_customers.csv",index=False)





