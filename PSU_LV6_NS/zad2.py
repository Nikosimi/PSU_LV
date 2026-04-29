from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from funkcija_6_1 import generate_data

X = generate_data(500, 1)

inertia = []

for k in range(1, 21):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(X)
    inertia.append(kmeans.inertia_)

plt.plot(range(1,21), inertia)
plt.xlabel("Br klastera")
plt.ylabel("Kriterijska funkcija")
plt.show()