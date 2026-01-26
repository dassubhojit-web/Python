'''Problem statement: Store Sales Quality Monitor (Statistics + Outlier Detection)
You are a data analyst for a retail store. Every day, you receive the total sales amount (or total revenue) for each store. 
Your manager wants a quick statistical health-check to understand:
Central tendency: Mean, Median, Mode

Spread: Standard Deviation
Distribution & outliers: Box-and-Whisker plot
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

print("This Python Programme is Store Sales Quality Monitor")
