import pandas as pd
df6=pd.read_csv("blinkit_customer_feedback.csv")
# print(df1.isnull().sum())
# df1=df1.drop_duplicates(subset=["order_id"])
df6=df6.drop_duplicates(subset=["feedback_id"])
Q1=df6["rating"].quantile(0.25)
Q3=df6["rating"].quantile(0.75)
IQR=Q3-Q1
lower=Q1-1.5*IQR
upper=Q3+1.5*IQR
Outliers=df6[(df6["rating"]<lower)|(df6["rating"]>upper)]
# print(Outliers)#No removing outliers because ratings can be 1 easily
# print(df6[(df6["rating"]>5)&(df6["rating"]<1)])
# print(df6["rating"].value_counts())

# Analysis
# 1)Average rating
avg_rating=df6["rating"].mean()
print("The average rating is:",avg_rating)
# 2)Best feedback category
best_feedb_catg=df6.groupby("feedback_category")["rating"].mean().sort_values(ascending=False).head(1)
print(best_feedb_catg)
# 3)Rating distribution
rating_distribution=df6["rating"].value_counts().sort_index(ascending=False)
print(rating_distribution)
df6.to_csv("cleaned_customer_feedback.csv",index=False)