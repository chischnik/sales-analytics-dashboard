import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming the CSV file is in the same directory as your script
data = pd.read_csv('sales_data.csv')

print(data.head())        # Display the first few rows
print(data.info())        # Summary of data types and missing values
print(data.describe())    # Descriptive statistics

# Check for and handle missing values or outliers
data = data.dropna()  # Example: Drop rows with missing values

# Total revenue per product
product_revenue = data.groupby('Product')['Revenue'].sum().sort_values(ascending=False)

# Monthly revenue trends
data['Date'] = pd.to_datetime(data['Date'])
data['Month'] = data['Date'].dt.month
monthly_revenue = data.groupby('Month')['Revenue'].sum()

# Plotting total revenue per product
plt.figure(figsize=(10, 6))
sns.barplot(x=product_revenue.index, y=product_revenue.values, palette='viridis')
plt.title('Total Revenue per Product')
plt.xlabel('Product')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)
plt.show()

# Plotting monthly revenue trends
plt.figure(figsize=(10, 6))
monthly_revenue.plot(kind='line', marker='o', color='blue')
plt.title('Monthly Revenue Trends')
plt.xlabel('Month')
plt.ylabel('Total Revenue')
plt.show()
