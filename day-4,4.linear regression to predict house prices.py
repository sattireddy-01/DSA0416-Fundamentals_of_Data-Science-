import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Sample data (replace with your actual dataset)
data = {
    'house_size': [1500, 1800, 1350, 2000, 1200, 1700, 1450, 1550, 1650],
    'house_prices': [300000, 350000, 280000, 400000, 250000, 320000, 290000, 310000, 330000]
}

df = pd.DataFrame(data)

# Bivariate analysis - scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(df['house_size'], df['house_prices'], color='blue', label='Data points')
plt.title('House Size vs House Prices')
plt.xlabel('House Size (sq ft)')
plt.ylabel('House Prices ($)')
plt.legend()
plt.grid(True)
plt.show()

# Prepare data for modeling
X = df[['house_size']]  # Feature (predictor variable)
y = df['house_prices']  # Target variable

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate model performance
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error (MSE): {mse:.2f}')
print(f'R-squared (R2) Score: {r2:.2f}')

# Plotting the regression line
plt.figure(figsize=(8, 6))
plt.scatter(X_test, y_test, color='blue', label='Test data')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Predicted regression line')
plt.title('Linear Regression: House Size vs House Prices')
plt.xlabel('House Size (sq ft)')
plt.ylabel('House Prices ($)')
plt.legend()
plt.grid(True)
plt.show()
