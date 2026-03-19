import numpy as np
import matplotlib.pyplot as plt

img=plt.imread("tiger.png")

bright=img+0.5
plt.imshow(bright)
rotated=np.rot90(img, k=-1)
plt.imshow(rotated)
mirror=np.fliplr(img)
plt.imshow(mirror)
small=img[::10,::10]
plt.imshow(small)

plt.show()

