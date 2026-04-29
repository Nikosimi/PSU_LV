from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt
from funkcija_6_1 import generate_data

X = generate_data(500, 1)

Z = linkage(X, method='ward')

dendrogram(Z)
plt.show()