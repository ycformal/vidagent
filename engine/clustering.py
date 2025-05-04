from sklearn.cluster import KMeans
from kneed import KneeLocator
import numpy as np

def cluster(arr):
    k_range = range(1, len(arr) + 1)
    X = np.array(arr).reshape(-1, 1)
    wcss = []

    # Compute WCSS for each k
    for k in k_range:
        kmeans = KMeans(n_clusters=k, random_state=0).fit(X)
        wcss.append(kmeans.inertia_)  # Inertia = WCSS

    # Use KneeLocator to find optimal k
    knee = KneeLocator(k_range, wcss, curve="convex", direction="decreasing")
    best_k = knee.knee or 1
    print(arr, best_k)

    # Final clustering
    kmeans = KMeans(n_clusters=best_k, random_state=0).fit(X)
    labels = kmeans.labels_

    # Organize output
    clusters = [[] for _ in range(best_k)]
    for val, label in zip(arr, labels):
        clusters[label].append(val)

    clusters = [sorted(c) for c in clusters]
    return clusters
