from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import numpy as np

# Step 1: Load the Iris dataset
iris = load_iris()
X = iris.data  # Features: sepal length, sepal width, petal length, petal width
y = iris.target  # Target: species (0: setosa, 1: versicolor, 2: virginica)

# Step 2: Split the data into training and testing sets (optional for this demo)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Initialize Decision Tree classifier
dt_classifier = DecisionTreeClassifier(random_state=42)

# Step 4: Train the classifier on the entire dataset (in this demo)
dt_classifier.fit(X, y)

# Function to predict based on user input features
def predict_iris_species(sepal_length, sepal_width, petal_length, petal_width):
    new_flower = np.array([[sepal_length, sepal_width, petal_length, petal_width]])  # Reshape to match X shape
    prediction = dt_classifier.predict(new_flower)
    species = iris.target_names[prediction[0]]
    return species

# Example usage:
# User input for new flower features
sepal_length = 5.1
sepal_width = 3.5
petal_length = 1.4
petal_width = 0.2

# Predict using Decision Tree classifier
predicted_species = predict_iris_species(sepal_length, sepal_width, petal_length, petal_width)
print(f"Predicted species for the new flower: {predicted_species}")
