from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import numpy as np

# Step 1: Load a sample dataset (e.g., Iris dataset)
dataset = load_iris()
X = dataset.data
y = dataset.target

# Step 2: Split dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Train a model (Example: Logistic Regression)
model = LogisticRegression()
model.fit(X_train, y_train)

# Function to evaluate model performance
def evaluate_model_performance(model, X_test, y_test):
    # Step 4: Make predictions on the test set
    y_pred = model.predict(X_test)
    
    # Calculate evaluation metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted')
    recall = recall_score(y_test, y_pred, average='weighted')
    f1 = f1_score(y_test, y_pred, average='weighted')
    
    return accuracy, precision, recall, f1

# Example usage:
# Prompt user to input feature names and target variable
print("Available features:", dataset.feature_names)
print("Target variable:", dataset.target_names)
print()

# Assuming user selects features and target for evaluation
selected_features = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
selected_target = 'target'

# Find corresponding feature indices in dataset
feature_indices = [list(dataset.feature_names).index(feature) for feature in selected_features]

# Subset X_test to selected features
X_test_selected = X_test[:, feature_indices]

# Evaluate model performance
accuracy, precision, recall, f1 = evaluate_model_performance(model, X_test_selected, y_test)

# Display evaluation results
print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1-score: {f1:.2f}")
