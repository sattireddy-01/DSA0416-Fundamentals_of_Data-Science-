import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset (replace this with your actual dataset)
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Temperature': [25, 28, 30, 32, 35, 34, 32, 31, 30, 28, 26, 24],
    'Rainfall': [50, 40, 30, 20, 10, 5, 5, 10, 20, 30, 40, 50]
}

df = pd.DataFrame(data)

# Line plot for temperature
plt.figure(figsize=(10, 6))
plt.plot(df['Month'], df['Temperature'], marker='o', color='red', linestyle='-')
plt.title('Monthly Temperature')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Line plot for rainfall
plt.figure(figsize=(10, 6))
plt.plot(df['Month'], df['Rainfall'], marker='o', color='blue', linestyle='-')
plt.title('Monthly Rainfall')
plt.xlabel('Month')
plt.ylabel('Rainfall (mm)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Scatter plot for temperature and rainfall
plt.figure(figsize=(10, 6))
plt.scatter(df['Temperature'], df['Rainfall'], color='green')
plt.title('Temperature vs Rainfall')
plt.xlabel('Temperature (°C)')
plt.ylabel('Rainfall (mm)')
plt.grid(True)
plt.show()
