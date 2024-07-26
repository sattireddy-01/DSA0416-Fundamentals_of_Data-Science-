import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Sample data (replace with your actual transaction data)
data = {
    'CustomerID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'TotalAmount': [100, 250, 80, 300, 150, 200, 120, 180, 210, 90],
    'NumItems': [2, 5, 1, 6, 3, 4, 2, 3, 4, 1]
}

df = pd.DataFrame(data)

# Standardize the features (TotalAmount and NumItems)
scaler = StandardScaler()
scaled_features = scaler.fit_transform(df[['TotalAmount', 'NumItems']])

# Fit PCA for dimensionality reduction (optional)
pca = PCA(n_components=2)
principal_components = pca.fit_transform(scaled_features)

# Convert to DataFrame
df_scaled = pd.DataFrame(data=principal_components, columns=['PCA1', 'PCA2'])

# Visualize the standardized data
plt.scatter(df_scaled['PCA1'], df_scaled['PCA2'])
plt.xlabel('PCA1')
plt.ylabel('PCA2')
plt.title('Standardized Data')
plt.show()

# Choose K based on elbow method or silhouette score
k = 3

# Train K-Means model
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(df_scaled)

# Add cluster labels to original DataFrame
df['Cluster'] = kmeans.labels_

# Visualize clusters
plt.scatter(df_scaled['PCA1'], df_scaled['PCA2'], c=df['Cluster'], cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], marker='x', color='red', s=300, label='Centroids')
plt.xlabel('PCA1')
plt.ylabel('PCA2')
plt.title('K-Means Clustering')
plt.legend()
plt.show()

# Analyze cluster centroids
cluster_centers = scaler.inverse_transform(kmeans.cluster_centers_)
centroid_df = pd.DataFrame(cluster_centers, columns=['TotalAmount', 'NumItems'])

# Print cluster centroids
print("Cluster Centroids:")
print(centroid_df)

# Analyze cluster sizes
cluster_counts = df['Cluster'].value_counts().sort_index()
print("\nCluster Sizes:")
print(cluster_counts)

# Plot cluster distribution
plt.bar(cluster_counts.index, cluster_counts.values)
plt.xlabel('Cluster')
plt.ylabel('Number of Customers')
plt.title('Cluster Sizes')
plt.show()
