import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

X, y = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

k_means = KMeans(n_clusters=4)
k_means.fit(X)
y_means = k_means.predict(X)

plt.figure(figsize=(10, 8))
plt.scatter(X[:, 0], X[:, 1], c=y_means, s=50, cmap='viridis')

center = k_means.cluster_centers_
plt.scatter(center[:, 0], center[:, 1], c='red', s=200, marker='X', label='Centroids')

plt.title("K-Means Clustering")
plt.legend(loc='upper right')

plt.xlabel('Feature 1')
plt.ylabel('Feature 2')

plt.savefig("Images/kmeans_clustering.png")


from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

data = load_iris()

X = data.data
y = data.target

pca = PCA(n_components=2)
x_pca = pca.fit_transform(X)

plt.figure(figsize=(10, 8))
scatter = plt.scatter(x_pca[:, 0], x_pca[:, 1], c=y, cmap='viridis', s=50)

plt.colorbar(scatter)
plt.title('PCA - Iris Dataset (2D)')

plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')

plt.savefig("Images/pca_iris.png")