import matplotlib.image as mpimg
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

img = mpimg.imread('example.png')
X = img.reshape(-1, 3)

kmeans = KMeans(n_clusters=25)
labels = kmeans.fit_predict(X)
colors = kmeans.cluster_centers_

compressed = colors[labels]
compressed = compressed.reshape(img.shape)

plt.subplot(1, 2, 1)
plt.imshow(img)

plt.subplot(1, 2, 2)
plt.imshow(compressed)
plt.show()