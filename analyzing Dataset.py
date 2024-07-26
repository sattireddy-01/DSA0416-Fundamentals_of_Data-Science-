import pandas as pd

# Load the dataset into a DataFrame
data = {
    'OrderID': [1, 2, 3, 4, 5],
    'CustomerID': [101, 102, 103, 104, 105],
    'ProductID': [101, 102, 103, 104, 105],
    'Quantity': [2, 1, 3, 2, 1],
    'TotalPrice': [20, 30, 45, 40, 15]
}

df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame with customer order information:")
print(df)
print()

# Basic statistics
print("Basic statistics:")
print(df.describe())
print()

# Total sales
total_sales = df['TotalPrice'].sum()
print("Total Sales: $" + str(total_sales))
print()

# Average quantity per order
avg_quantity = df['Quantity'].mean()
print("Average Quantity per Order:", avg_quantity)
print()

# Most popular products (by total quantity sold)
popular_products = df.groupby('ProductID')['Quantity'].sum().sort_values(ascending=False).head(3)
print("Most Popular Products (by total quantity sold):")
print(popular_products)
print()

# Customer with the highest total spending
top_customer = df.groupby('CustomerID')['TotalPrice'].sum().idxmax()
top_customer_spending = df.groupby('CustomerID')['TotalPrice'].sum().max()
print("Customer with the Highest Total Spending:")
print("Customer ID:", top_customer)
print("Total Spending: $" + str(top_customer_spending))
