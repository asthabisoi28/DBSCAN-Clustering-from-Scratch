import numpy as np

class DBSCAN:
    def __init__(self, eps, min_samples):
        self.eps = eps
        self.min_samples = min_samples

    def _distance(self, p1, p2):
        return np.linalg.norm(p1 - p2)

    def _region_query(self, X, idx):
        neighbors = []
        for i in range(len(X)):
            if self._distance(X[idx], X[i]) <= self.eps:
                neighbors.append(i)
        return neighbors

    def _expand_cluster(self, X, labels, visited, idx, neighbors, cluster_id):
        labels[idx] = cluster_id

        i = 0
        while i < len(neighbors):
            point = neighbors[i]

            if not visited[point]:
                visited[point] = True
                new_neighbors = self._region_query(X, point)

                if len(new_neighbors) >= self.min_samples:
                    neighbors.extend(new_neighbors)

            if labels[point] == -1:
                labels[point] = cluster_id

            i += 1

    def fit(self, X):
        n = len(X)
        labels = np.full(n, -1)
        visited = np.zeros(n, dtype=bool)

        cluster_id = 0

        for i in range(n):
            if visited[i]:
                continue

            visited[i] = True
            neighbors = self._region_query(X, i)

            if len(neighbors) < self.min_samples:
                labels[i] = -1
            else:
                self._expand_cluster(X, labels, visited, i, neighbors, cluster_id)
                cluster_id += 1

        return labels
