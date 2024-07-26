import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample dataset (replace this with your actual dataset)
data = {
    'ProductCategory': ['Electronics', 'Clothing', 'Books', 'Electronics', 'Books', 'Clothing', 'Books', 'Electronics', 'Clothing'],
    'Sales': [10000, 15000, 8000, 12000, 9000, 16000, 7000, 11000, 17000]
}

df = pd.DataFrame(data)

# Calculate total sales per product category
sales_by_category = df.groupby('ProductCategory')['Sales'].sum().reset_index()

# Line plot
plt.figure(figsize=(10, 6))
sns.lineplot(x='ProductCategory', y='Sales', data=sales_by_category, marker='o')
plt.title('Sales Distribution across Product Categories (Line Plot)') 
plt.xlabel('Product Category')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='ProductCategory', y='Sales', data=sales_by_category, s=100)
plt.title('Sales Distribution across Product Categories (Scatter Plot)')
plt.xlabel('Product Category')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Bar plot
plt.figure(figsize=(10, 6))
sns.barplot(x='ProductCategory', y='Sales', data=sales_by_category)
plt.title('Sales Distribution across Product Categories (Bar Plot)')
plt.xlabel('Product Category')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
