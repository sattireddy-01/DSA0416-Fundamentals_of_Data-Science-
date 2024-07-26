import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score

# Sample customer data (replace with your actual dataset)
data = {
    'CustomerID': [1, 2, 3, 4, 5],
    'Age': [25, 30, 35, 40, 45],
    'AnnualIncome': [50000, 60000, 75000, 80000, 40000],
    'SpendingScore': [50, 80, 75, 90, 30]
}

df = pd.DataFrame(data)

# Select features for clustering
X = df[['Age', 'AnnualIncome', 'SpendingScore']]

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply K-means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(X_scaled)

# Add cluster labels to the original dataframe
df['Cluster'] = clusters

# Visualize clusters using PCA for dimensionality reduction
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

plt.figure(figsize=(8, 6))
scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=clusters, cmap='viridis', s=100, alpha=0.8, label=clusters)
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('Customer Segmentation using K-means Clustering')
plt.legend(*scatter.legend_elements(), title='Clusters')
plt.grid(True)
plt.show()

# Optional: Evaluate clustering performance using silhouette score
silhouette_avg = silhouette_score(X_scaled, clusters)
print(f"Silhouette Score: {silhouette_avg:.2f}")

# Display the segmented customer data
print("\nSegmented Customer Data:")
print(df)
