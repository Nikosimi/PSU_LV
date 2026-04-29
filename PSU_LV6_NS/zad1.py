from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from funkcija_6_1 import generate_data

X = generate_data(500, 1)

kmeans = KMeans(n_clusters=3)
labels = kmeans.fit_predict(X)
centers = kmeans.cluster_centers_

plt.scatter(X[:,0], X[:,1], c=labels)
plt.scatter(centers[:,0], centers[:,1], c='red', marker='x')
plt.show()
