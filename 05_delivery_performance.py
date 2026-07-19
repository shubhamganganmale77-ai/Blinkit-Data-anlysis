import pandas as pd
df5=pd.read_csv("blinkit_delivery_performance.csv")
# print(df5.isnull().sum())#reasone_if delayed consist null values but we cant remove them because of reasone is only given if delivery is delayed. And other columns does not consists null values
del_min=df5[df5["delivery_time_minutes"]<0]#Here are the negative valuer in this column we cant remove them because they are delivered before the time
print(df5.info())
df5["promised_time"]=pd.to_datetime(df5["promised_time"],errors="coerce")
df5["actual_time"]=pd.to_datetime(df5["actual_time"],errors="coerce")
# print(df5["promised_time"].isnull().value_counts())
# print(df5["actual_time"].isnull().value_counts())
Q1=df5["delivery_time_minutes"].quantile(0.25)
Q3=df5["delivery_time_minutes"].quantile(0.75)
IQR=Q3-Q1
lower=Q1-1.5*IQR
upper=Q3+1.5*IQR
Outliers=df5[(df5["delivery_time_minutes"]<lower)|(df5["delivery_time_minutes"]>upper)]#No remove outliers bcz max delivery time is 30 which is possible
print(Outliers["delivery_time_minutes"].value_counts())

# Analysis
# 1)Average delivery delay as per delayed delivery
avg_delay_time=df5[df5["delivery_time_minutes"]>0]
print("average delay time is:",avg_delay_time["delivery_time_minutes"].mean(),"(in minutes)")
# 2)Average early delivery time as per early delivered deliveries
avg_early_time=df5[df5["delivery_time_minutes"]<0]
print("average delay time is:",avg_early_time["delivery_time_minutes"].mean(),"('-'indicates early)")
# 3)common reasones for delay
reasons=df5["reasons_if_delayed"].value_counts()
print("The reasone for delay with number of time:\n",reasons)
print(df5.info())
# 4)Delivery partner id with most delayed deliveries
del_partner=df5.groupby("delivery_partner_id")["reasons_if_delayed"].count().sort_values(ascending=False)
print(del_partner)
df5.to_csv("cleaned_delivery_performance.csv",index=False)