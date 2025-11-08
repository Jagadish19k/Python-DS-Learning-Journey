# Python Practice File - pandas

import pandas as pd
import numpy as np

# ----------------------------------------------------
# 1. DataFrame Creation and Inspection
# ----------------------------------------------------

# Create a DataFrame (DF) from a dictionary of lists
data = {
    'UserID': [101, 102, 103, 104, 105, 106, 107],
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Laptop', 'Monitor', 'Mouse', 'Webcam'],
    'Price': [1200, 25, 75, np.nan, 300, 25, 50],
    'Region': ['East', 'West', 'East', 'Central', 'West', 'East', 'Central'],
    'Rating': [4.5, 3.8, 4.2, 4.9, 4.0, np.nan, 4.1]
}
df = pd.DataFrame(data)

print("--- 1. DataFrame Creation and Inspection ---")
print("First 3 rows (.head()):")
print(df.head(3))

print("\nDataFrame Information (.info()):")
# .info() provides a summary, including data types and non-null counts
df.info()

print(f"\nDataFrame Shape (Rows, Columns): {df.shape}")
print("-" * 50)

# ----------------------------------------------------
# 2. Selection and Filtering (Subsetting)
# ----------------------------------------------------
print("--- 2. Selection and Filtering ---")

# Simple Column Selection (Series)
product_col = df['Product']
print("\nProduct Column (Series):\n", product_col.head())

# Multi-Column Selection (DataFrame)
subset_df = df[['UserID', 'Price', 'Region']]
print("\nUserID, Price, and Region Subset:\n", subset_df.head())

# Filtering (Boolean Indexing) - Products priced under 100
low_cost = df[df['Price'] < 100]
print("\nLow Cost Products (Price < 100):\n", low_cost)

# Filtering with multiple conditions (using & for AND, | for OR)
# Must use parentheses for each condition
high_rated_west = df[(df['Region'] == 'West') & (df['Rating'] > 3.9)]
print("\nHigh Rated Products in the West Region:\n", high_rated_west)
print("-" * 50)

# ----------------------------------------------------
# 3. Handling Missing Data (NaN)
# ----------------------------------------------------
print("--- 3. Handling Missing Data ---")

# Check for missing values
print("\nMissing values count:\n", df.isnull().sum())

# Drop rows with ANY missing data (drops row 3 and 5)
df_dropped = df.dropna()
print("\nDataFrame after dropping NaN rows (.dropna()):\n", df_dropped)

# Fill missing values in the 'Price' column with the mean of the column
mean_price = df['Price'].mean()
df_filled = df.fillna({'Price': mean_price, 'Rating': df['Rating'].median()})
print("\nDataFrame after filling NaN (Price with Mean, Rating with Median):\n", df_filled)

print("-" * 50)

# ----------------------------------------------------
# 4. Grouping and Aggregation
# ----------------------------------------------------
print("--- 4. Grouping and Aggregation ---")

# Group by Region and calculate the mean and count of Price
region_summary = df.groupby('Region')['Price'].agg(['mean', 'count', 'min', 'max'])
print("\nPrice Summary by Region:\n", region_summary)

# Group by Product and calculate the total count of each
product_counts = df['Product'].value_counts()
print("\nProduct Counts (value_counts()):\n", product_counts)

print("-" * 50)

# ----------------------------------------------------
# 5. Merging (Joining DataFrames)
# ----------------------------------------------------
print("--- 5. Merging DataFrames ---")

# Create a second DataFrame for category lookup
category_data = {
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Webcam'],
    'Category': ['Electronics', 'Accessories', 'Accessories', 'Electronics', 'Accessories']
}
df_category = pd.DataFrame(category_data)

# Merge the original DF with the new category DF on the 'Product' column (inner join by default)
df_merged = pd.merge(df, df_category, on='Product', how='left')
print("\nDataFrame after Left Merge with Category:\n", df_merged)