import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Sample data (replace with your actual transaction data)
data = {
    'CustomerID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'TotalAmount': [100, 250, 80, 300, 150, 200, 120, 180, 210, 90],
    'Frequency': [3, 8, 1, 10, 5, 7, 4, 6, 7, 2]
}

df = pd.DataFrame(data)

# Select features for clustering
X = df[['TotalAmount', 'Frequency']]

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Determine optimal number of clusters (k) using elbow method
inertia = []
for k in range(1, 10):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)

plt.plot(range(1, 10), inertia, marker='o')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.title('Elbow Method for Optimal k')
plt.show()

# Choose k and train K-Means model
k = 3
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(X_scaled)

# Add cluster labels to original DataFrame
df['Cluster'] = kmeans.labels_

# Visualize clusters
plt.scatter(df['TotalAmount'], df['Frequency'], c=df['Cluster'], cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], marker='x', color='red', s=300, label='Centroids')
plt.xlabel('Total Amount Spent')
plt.ylabel('Frequency of Visits')
plt.title('Customer Segmentation based on Spending Patterns')
plt.legend()
plt.show()

# Analyze cluster centroids
cluster_centers = scaler.inverse_transform(kmeans.cluster_centers_)
centroid_df = pd.DataFrame(cluster_centers, columns=['TotalAmount', 'Frequency'])

# Print cluster centroids
print("Cluster Centroids:")
print(centroid_df)

# Analyze cluster sizes
cluster_counts = df['Cluster'].value_counts().sort_index()
print("\nCluster Sizes:")
print(cluster_counts)
