import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

# Sample data (replace with your actual dataset)
data = {
    'age': [45, 50, 35, 40, 55, 30, 42, 38, 48, 52],
    'gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Male', 'Female', 'Male', 'Female', 'Male'],
    'blood_pressure': [120, 130, 125, 115, 122, 118, 128, 132, 127, 121],
    'cholesterol': [200, 220, 190, 210, 195, 205, 215, 225, 190, 200],
    'treatment_outcome': ['Good', 'Bad', 'Good', 'Good', 'Bad', 'Good', 'Good', 'Bad', 'Good', 'Bad']
}

df = pd.DataFrame(data)

# Convert categorical variables to numerical (if needed)
df['gender'] = df['gender'].map({'Male': 0, 'Female': 1})

# Split data into features and target variable
X = df[['age', 'gender', 'blood_pressure', 'cholesterol']]
y = df['treatment_outcome']

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Build and train the KNN model
k = 3  # Number of neighbors
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train_scaled, y_train)

# Make predictions
y_pred = knn.predict(X_test_scaled)

# Evaluate model performance
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, pos_label='Good')
recall = recall_score(y_test, y_pred, pos_label='Good')
f1 = f1_score(y_test, y_pred, pos_label='Good')

print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1-score: {f1:.2f}")

# Display classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
