import pandas as pd
df1=pd.read_csv("blinkit_products.csv")
df1=df1.dropna()
df1=df1.drop_duplicates(subset="product_id")
Q1=df1["price"].quantile(0.25)
Q3=df1["price"].quantile(0.75)
IQR=Q3-Q1
lower=Q1-1.5*IQR
upper=Q3+1.5*IQR
Outliers=df1[(df1["price"]>upper)|(df1["price"]<lower)]
df1=df1[(df1["price"]<upper)&(df1["price"]>lower)]#Removing Outliers(No needed)

#Analysis
# 1)Most expensive products.
top5_expensive_product=df1[["product_name","price"]].sort_values(by="price",ascending=False).head(5).reset_index(drop=True)
print(top5_expensive_product)#.reset_index(drop=True) used to reset the indexes
# 2)Cheapest products.
top10_cheapest_products=df1[["product_name","price"]].sort_values(by="price").reset_index(drop=True).head(10)
print(top10_cheapest_products)
# 3)Average product price by category
Avg_price_per_category=df1.groupby("category")["price"].mean().reset_index()
print(Avg_price_per_category)
# 4)Highest margin brands.
Highest_margin_brands=df1[["brand","margin_percentage"]].sort_values(by="margin_percentage",ascending=False)
max_margin=Highest_margin_brands["margin_percentage"].max()
Highest_margin_brands=Highest_margin_brands[Highest_margin_brands["margin_percentage"]==max_margin]
print(Highest_margin_brands)#340 brands are about highest(same) margin
# 5)Category with the most products
most_products_with_category=df1["category"].value_counts().sort_values(ascending=False).head(5)
print("Categories with most product are:\n",most_products_with_category)
df1.to_csv("cleaned_products.csv",index=False)
