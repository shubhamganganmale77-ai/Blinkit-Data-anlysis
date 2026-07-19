import pandas as pd 
df9=pd.read_csv("blinkit_marketing_performance.csv")
df9["date"]=pd.to_datetime(df9["date"],errors="coerce")
invalid_campaign_id=df9["campaign_id"]>0
invalid_revenue=df9["revenue_generated"]<=0
# print(invalid_revenue.value_counts())
duplicate_campaign_id=df9.duplicated(subset="campaign_id")
# print(duplicate_campaign_id.value_counts())#No duplicate entries
# print(df9["campaign_name"].isnull().value_counts())
Q1=df9["clicks"].quantile(0.25)
Q3=df9["clicks"].quantile(0.75)
IQR=Q3-Q1
lower=Q1-1.5*IQR
upper=Q3+1.5*IQR
Outliers1=df9[(df9["clicks"]>upper)|(df9["clicks"]<lower)]
# print(Outliers)#no outlier detected
Q1=df9["spend"].quantile(0.25)
Q3=df9["spend"].quantile(0.75)
IQR=Q3-Q1
lower=Q1-1.5*IQR
upper=Q3+1.5*IQR
Outliers2=df9[(df9["spend"]>upper)|(df9["spend"]<lower)]
# print(Outliers2)#No outlier detected

# Analysis
# 1)Campaign with highest ROAS
max_roas=df9["roas"].max()
campaign=df9[["campaign_id","campaign_name","roas"]]
campaign=campaign[campaign["roas"]==max_roas]
print("These are the campaigns with the highest ROAS",campaign)
# 2)Highest revenue campaign.
print(df9.info())
camp_revenue=df9[["campaign_id","campaign_name","revenue_generated"]].sort_values(by="revenue_generated",ascending=False).head(1)
print("Campaign with the highest revenue:\n",camp_revenue)
# 3)Highest CTR(click through rate)=clicks/impressions*100
ctr=df9[["campaign_id","campaign_name","clicks","impressions"]]
ctr["CTR"]=(ctr["clicks"]/ctr["impressions"])*100
ctr=ctr.sort_values(by="CTR",ascending=False).head(1).reset_index(drop=True)
print("campaign with highest CTR id:\n",ctr)
df9.to_csv("cleaned_marketing_performance.csv",index=False)