import numpy as np
import matplotlib.pyplot as plt

def chequer(size, height, width):
    black=np.zeros((size, size))
    white=np.ones((size, size))*255

    rows=[]

    for i in range(height):
        row=[]
        for j in range(width):
            if(i+j)%2==0:
                row.append(black)
            else:
                row.append(white)
            
        rows.append(np.hstack(row))
    img = np.vstack(rows)

    return img

img=chequer(50, 4, 5)

plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.show()

