import pandas as pd
from sklearn.tree import DecisionTreeRegressor, export_text

# Sample data (replace with your actual dataset)
data = {
    'mileage': [50000, 60000, 30000, 70000, 20000],
    'age': [3, 5, 2, 6, 1],
    'brand': ['Toyota', 'Honda', 'Toyota', 'Ford', 'Honda'],
    'engine_type': ['Petrol', 'Diesel', 'Petrol', 'Petrol', 'Hybrid'],
    'price': [25000, 18000, 30000, 15000, 28000]
}

df = pd.DataFrame(data)

# Dummy encoding for categorical variables
df = pd.get_dummies(df, columns=['brand', 'engine_type'])

# Features and target variable
X = df.drop('price', axis=1)
y = df['price']

# Build CART Regression Model
model = DecisionTreeRegressor(random_state=42)
model.fit(X, y)

# Function to predict price and display decision path
def predict_price(mileage, age, brand, engine_type):
    # Create input data for prediction
    # Ensure all possible categories are included in input_df
    possible_brands = ['Toyota', 'Honda', 'Ford']
    possible_engine_types = ['Petrol', 'Diesel', 'Hybrid']

    input_data = {
        'mileage': [mileage],
        'age': [age],
        'brand': [brand] if brand in possible_brands else ['Toyota'],  # Default to 'Toyota'
        'engine_type': [engine_type] if engine_type in possible_engine_types else ['Petrol']  # Default to 'Petrol'
    }
    input_df = pd.DataFrame(input_data)

    # Dummy encode categorical variables for prediction
    input_df = pd.get_dummies(input_df, columns=['brand', 'engine_type'])

    # Align input_df with X to ensure consistent columns
    input_df = input_df.reindex(columns=X.columns, fill_value=0)

    # Predict price
    predicted_price = model.predict(input_df)[0]

    # Display decision path
    tree_rules = export_text(model, feature_names=list(X.columns))

    print(f"Predicted Price: ${predicted_price:.2f}")
    print("Decision Path:")
    print(tree_rules)

# Example usage
print("Example Usage:")
predict_price(mileage=45000, age=4, brand='Toyota', engine_type='Petrol')
