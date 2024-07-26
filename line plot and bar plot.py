import matplotlib.pyplot as plt
import pandas as pd

# Sample dataset (replace this with your actual dataset)
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Sales': [10000, 12000, 11000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 2000, 21000]
}

df = pd.DataFrame(data)

# Extract month and sales values
months = df['Month']
sales = df['Sales']

# Create line plot
plt.figure(figsize=(10, 6))
plt.plot(months, sales, marker='o', color='blue', linestyle='-')
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Create bar plot
plt.figure(figsize=(10, 6))
plt.bar(months, sales, color='green')
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()
