from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import numpy as np

# Sample data (replace with your actual dataset)
# Assume X contains symptom features and y contains labels (0 or 1)
X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])  # Example features
y = np.array([0, 1, 0, 1])  # Example labels (0: no condition, 1: condition)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize KNN classifier (you can set k as needed)
k = 3  # Number of neighbors (you can take this as user input)
knn_classifier = KNeighborsClassifier(n_neighbors=k)

# Train the KNN classifier
knn_classifier.fit(X_train, y_train)

# Function to predict based on user input features
def predict_condition(symptoms, k):
    new_patient = np.array(symptoms).reshape(1, -1)  # Reshape to match X shape
    prediction = knn_classifier.predict(new_patient)
    if prediction[0] == 0:
        return "No medical condition"
    elif prediction[0] == 1:
        return "Medical condition detected"

# Example usage:
# User input for new patient symptoms
new_patient_symptoms = [3, 4, 5]  # Replace with actual user input

# Predict using KNN classifier
prediction_result = predict_condition(new_patient_symptoms, k)
print(f"Prediction for new patient: {prediction_result}")
