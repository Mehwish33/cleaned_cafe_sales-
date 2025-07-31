import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df=pd.read_csv("C:\\Users\\MEHWISH\\Downloads\\dirty_cafe_sales.csv")
# print(df.head())
# df=pd.read_csv("C:\\Users\\User\\Downloads\\netflix1.csv")
print(f"whole data is: \n {df.head()}")
print("--------------------------------")
print(df.info)
print("---------------------------------")
print(df.describe())
print("---------------------------------")
print("here are null values\n")
print(df.isnull().sum().sort_values(ascending=False))
print("----------------------------------")
print("here are duplicate: ")
print(df.duplicated().sum())
print("-------------------------------")

# convert columns to numeric
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
df['Price Per Unit'] = pd.to_numeric(df['Price Per Unit'], errors='coerce')
df['Total Spent'] = pd.to_numeric(df['Total Spent'], errors='coerce')
# drop rows with missing value

df_cleaned=df.dropna(subset=["Item","Price Per Unit","Quantity","Total Spent"])

print(df_cleaned.isnull().sum().sort_values(ascending=False))
# fill missing values for catagorecial columns


item_mod=df_cleaned["Item"].mode()[0]
print("--------------------------------")
print(item_mod)
loc_mod=df_cleaned["Location"].mode()[0]
print(loc_mod)
print("-----------------------------")
df_cleaned["Item"]=df_cleaned["Item"].fillna(item_mod)
df_cleaned["Location"]=df_cleaned["Location"].fillna(loc_mod)
print("------------------------------------")
print(f" data after filling and dropping missing values: \n {df_cleaned}")
print(df_cleaned.isnull().sum().sort_values(ascending=False))

# Remove duplicates rows
df_cleaned=df_cleaned.drop_duplicates()
print("-----------------------------------")
print(f"here data is without duplicates: \n {df_cleaned} ")

# convert transaction date to datetime to find unknown
df_cleaned["Transaction Date"]=pd.to_datetime(df_cleaned["Transaction Date"],errors="coerce")
df_cleaned["Transaction Date"]=df_cleaned["Transaction Date"].dt.strftime("%Y-%m-%d")
print("-----------------------------------------")
print(f"here data is aftered converted to datetime: \n {df_cleaned}")


# imputing outliers by IQR method
Q1=np.percentile(df_cleaned["Total Spent"],25,interpolation="midpoint")
Q3=np.percentile(df_cleaned["Total Spent"],75,interpolation="midpoint")

IQR=Q3-Q1

lowerbond=Q1-(1.5*IQR)
upperbond=Q3+(1.5*IQR)
print("--------------------------")
print(f"lowerbond is: \n {lowerbond}")
print(f"upperbond is: \n {upperbond}")
print("---------------------------")
print(f" here data is with outliers: \n {df_cleaned}")
print("---------------------------------------")
print(f" Here outliers are based on IQR :\n {df_cleaned[(df_cleaned['Total Spent']<lowerbond)|(df_cleaned['Total Spent']>upperbond)]}")
# remove uotliers
df_cleaned=df_cleaned[(df["Total Spent"]>=lowerbond)&(df_cleaned["Total Spent"]<=upperbond)]
print(f" Here data without outliers : \n {df_cleaned}")


df_cleaned.to_csv(r"C:\\Users\\Mehwish\Documents\\cleaned_cafe_sales.csv",index=False)








