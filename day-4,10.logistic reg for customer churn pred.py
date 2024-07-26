from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import numpy as np

# Sample dataset (replace with your actual dataset)
# Assume X contains features and y contains churn status (0 or 1)
# Example data for demonstration
X = np.array([[100, 12], [200, 24], [300, 36], [400, 48], [500, 60]])  # Features: usage minutes, contract duration
y = np.array([0, 0, 1, 1, 1])  # Target: churn status (0: not churned, 1: churned)

# Step 3: Initialize Logistic Regression model
logreg_model = LogisticRegression()

# Step 4: Train the model on the dataset
logreg_model.fit(X, y)

# Function to predict based on user input features
def predict_churn(usage_minutes, contract_duration):
    new_customer = np.array([[usage_minutes, contract_duration]])
    prediction = logreg_model.predict(new_customer)
    if prediction[0] == 1:
        return "Churned"
    else:
        return "Not Churned"

# Example usage:
# User input for new customer features
usage_minutes = 250
contract_duration = 20

# Predict using Logistic Regression model
predicted_churn_status = predict_churn(usage_minutes, contract_duration)
print(f"Predicted churn status for the new customer: {predicted_churn_status}")
