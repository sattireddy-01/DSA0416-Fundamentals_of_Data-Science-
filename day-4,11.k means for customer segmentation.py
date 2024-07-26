from sklearn.cluster import KMeans
import numpy as np

# Sample dataset (replace with your actual dataset)
# Assume X contains features related to shopping behavior
# Example data for demonstration
X = np.array([[10, 20], [15, 25], [25, 30], [30, 40], [8, 15], [35, 45]])

# Step 2: Initialize K-Means model
kmeans_model = KMeans(n_clusters=3, random_state=42)  # Assuming 3 clusters for demonstration

# Step 3: Train the model on the dataset
kmeans_model.fit(X)

# Function to predict customer segment based on input features
def predict_customer_segment(shopping_feature1, shopping_feature2):
    new_customer = np.array([[shopping_feature1, shopping_feature2]])
    predicted_segment = kmeans_model.predict(new_customer)
    return predicted_segment[0]

# Example usage:
# User input for new customer features
shopping_feature1 = 20
shopping_feature2 = 25

# Predict using K-Means clustering model
predicted_segment = predict_customer_segment(shopping_feature1, shopping_feature2)
print(f"Predicted segment for the new customer: {predicted_segment}")
