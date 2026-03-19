import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(open("mtcars.csv", "rb"), usecols=(1,2,3,4,5,6), delimiter=",", skiprows=1)
mpg = data[:,0]
hp = data[:,3]
wt = data[:,5]
print(mpg.ndim)
plt.scatter(hp, mpg, s=wt*50)
print("svi cilindri min: ",mpg.min())
print("svi cilindri max: ",mpg.max())
print("svi cilindri mean: ",mpg.mean())

cyl=data[:,1]
mpg6=mpg[cyl==6]
print("6 cyl min: ",mpg6.min())
print("6 cyl max: ",mpg6.max())
print("6 cyl mean: ",mpg6.mean())

print("Srednja vrijednost hp: ", hp.mean())
mpg8=mpg[cyl==8]
print("Srednja vrijednost potrosnje s 8 cilindara: ", mpg8.mean())

plt.show()

