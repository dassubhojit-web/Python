'''Problem statement: Store Sales Quality Monitor (Statistics + Outlier Detection)
You are a data analyst for a retail store. Every day, you receive the total sales amount (or total revenue) for each store. 
Your manager wants a quick statistical health-check to understand:
Central tendency: Mean, Median, Mode Spread: Standard Deviation Distribution & outliers: Box-and-Whisker plot
Anomaly detection: Z-score to flag abnormal days/stores
Your tasks
Using the sample data below, write Python code to:
Load the data into a DataFrame
Compute mean, median, mode of sales_amount
Compute standard deviation
Create a box-and-whisker plot
Compute z-score for each record
Flag records where |z| > 2 as outliers
Print a final table of outliers (date, store, sales, z-score)'''

import pandas as pd
import matplotlib.pyplot as plt

print("This python programme is for store sales quality monitor")
storedata=pd.read_csv("store_daily_sales.csv")
print(storedata.head())
sales_amount_mean=storedata.iloc[:, 2].mean()
sales_amount_median=storedata.iloc[:, 2].median()
sales_amount_mode=storedata.iloc[:, 2].mode().tolist()
print(f"Here is the Sales Amount Mean\t {sales_amount_mean}\nHere is the Sales Amount Median\t {sales_amount_median}\nHere is the Sales Amount Mode\t {sales_amount_mode}")
sales_amount_sd=storedata.iloc[:, 2].std()
print(f"Here is the standard deviation\t {sales_amount_sd}")

# Box-and-whisker plot for sales_amount (3rd column)
ax = storedata.iloc[:, 2].plot(kind="box", title="Sales Amount Box-and-Whisker")
ax.set_ylabel("Sales Amount")
ax.set_ylim(10000, 16000)  # adjust min/max as you want
plt.show()

sales_amount = storedata.iloc[:, 2]
sales_std = sales_amount.std(ddof=0)
storedata["z_score"] = (sales_amount - sales_amount.mean()) / sales_std
print(storedata[["z_score"]].head())
