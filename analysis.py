import pandas as pd

# Load dataset
data = pd.read_csv("data/sales.csv")

# Show first rows
print("Dataset Preview")
print(data.head())

# Total sales
total_sales = data["Sales"].sum()
print("Total Sales:", total_sales)

# Sales by category
category_sales = data.groupby("Category")["Sales"].sum()
print("\nSales by Category")
print(category_sales)

# Top selling product
top_product = data.groupby("Product")["Quantity"].sum().sort_values(ascending=False)
print("\nTop Selling Products")
print(top_product)