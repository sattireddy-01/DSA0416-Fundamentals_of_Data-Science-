import pandas as pd
import matplotlib.pyplot as plt
data = {
    'Date': [
        '2023-06-01', '2023-06-02', '2023-06-03', '2023-06-04', '2023-06-05', 
        '2023-06-06', '2023-06-07', '2023-06-08', '2023-06-09', '2023-06-10',
        '2023-06-11', '2023-06-12', '2023-06-13', '2023-06-14', '2023-06-15',
        '2023-06-16', '2023-06-17', '2023-06-18', '2023-06-19', '2023-06-20',
        '2023-06-21', '2023-06-22', '2023-06-23', '2023-06-24', '2023-06-25',
        '2023-06-26', '2023-06-27', '2023-06-28', '2023-06-29', '2023-06-30'
    ],
    'Sales': [
        100, 110, 105, 115, 120, 
        130, 125, 140, 145, 150, 
        155, 160, 165, 170, 175, 
        180, 185, 190, 195, 200, 
        205, 210, 215, 220, 225, 
        230, 235, 240, 245, 250
    ]
}
sales_data = pd.DataFrame(data)
sales_data['Date'] = pd.to_datetime(sales_data['Date'])

print(sales_data.head())


plt.figure(figsize=(10, 5))
plt.plot(sales_data['Date'], sales_data['Sales'], marker='o', linestyle='-', color='b')
plt.title('Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 5))
plt.scatter(sales_data['Date'], sales_data['Sales'], color='blue')
plt.title('Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 5))
plt.bar(sales_data['Date'], sales_data['Sales'], color='green')
plt.title('Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
