import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Sample dataset (replace with your actual dataset)
data = {
    'area': [1500, 1800, 2200, 1600, 1900],
    'bedrooms': [3, 4, 3, 2, 4],
    'price': [300000, 360000, 400000, 320000, 380000]
}

# Convert data to Pandas DataFrame
df = pd.DataFrame(data)

# Extract features and target variable
X = df[['area', 'bedrooms']].values  # Features: area and bedrooms
y = df['price'].values  # Target variable: price

# Create linear regression model
model = LinearRegression()

# Train the model
model.fit(X, y)

# Function to predict price based on user input
def predict_price(area, bedrooms):
    # Prepare input data
    X_new = np.array([[area, bedrooms]])  # Reshape input correctly
    
    # Predict price
    predicted_price = model.predict(X_new)
    
    return predicted_price[0]

# Example usage
area_input = 2000  # user input for area in sq. ft
bedrooms_input = 3  # user input for number of bedrooms

predicted_price = predict_price(area_input, bedrooms_input)
print(f"Predicted price for a house with {area_input} sq. ft and {bedrooms_input} bedrooms: ${predicted_price:.2f}")
