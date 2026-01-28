import numpy as np
import matplotlib.pyplot as plt
from dbscan import DBSCAN

np.random.seed(42)

# creating 3 clusters
cluster_1 = np.random.randn(50, 2) + np.array([2, 2])
cluster_2 = np.random.randn(50, 2) + np.array([8, 8])
cluster_3 = np.random.randn(50, 2) + np.array([8, 2])

# noise points
noise = np.random.uniform(0, 10, (10, 2))

X = np.vstack((cluster_1, cluster_2, cluster_3, noise))

dbscan = DBSCAN(eps=1.2, min_samples=5)
labels = dbscan.fit(X)

unique_labels = set(labels)

for label in unique_labels:
    if label == -1:
        plt.scatter(X[labels == label, 0],
                    X[labels == label, 1],
                    color='black',
                    label='Noise')
    else:
        plt.scatter(X[labels == label, 0],
                    X[labels == label, 1],
                    label=f'Cluster {label}')

plt.title("DBSCAN Clustering Result")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()
