import numpy as np
import matplotlib.pyplot as plt

img=plt.imread("/Users/nikos/Downloads/LV2-20260323/tiger.png")

bright=img+0.5
rotated=np.rot90(img, k=3)
mirror=np.fliplr(img)
small=img[::10,::10]
h,w,c = img.shape
rez=np.zeros_like(img)
first = w//4
last = w//2
rez[:, first:last] = img[:, first:last]

plt.imshow(bright)
plt.show()
plt.imshow(rotated)
plt.show()
plt.imshow(mirror)
plt.show()
plt.imshow(small)
plt.show()
plt.imshow(rez)
plt.show()


