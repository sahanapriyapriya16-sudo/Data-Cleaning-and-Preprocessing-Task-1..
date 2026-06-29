# Data Cleaning Project
# Author: Sahanapriya Anand

import pandas as pd

# Load the dataset
df = pd.read_csv("Mall_Customers.csv")

# Display basic information
print("Dataset Information:")
print(df.info())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows with missing values (if any)
df = df.dropna()

# Display cleaned dataset
print("\nCleaned Dataset Preview:")
print(df.head())

# Save the cleaned dataset
df.to_csv("cleaned_mall_customers.csv", index=False)

print("\nData cleaning completed successfully!")
print("Cleaned dataset saved as 'cleaned_mall_customers.csv'")
