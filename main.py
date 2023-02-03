import numpy as np
import matplotlib.pyplot as plt

from skimage.io import imread
from skimage.filters import roberts, sobel, scharr, prewitt

img = imread("gado.jpeg", as_gray=True) # mudar as imagem aqui no lugar do "andiroba.jpeg" ex: "abacaxi.jpeg" ou "gado.jpeg"
op_roberts = roberts(img)
op_sobel = sobel(img)
op_scharr = scharr(img)
op_prewitt = prewitt(img)

fig, axes = plt.subplots(nrows=2, ncols=2, sharex=True, sharey=True, figsize=(12, 12))

ax = axes.ravel()

ax[0].imshow(op_roberts, cmap=plt.cm.gray)
ax[0].set_title('Operador de Roberts')

ax[1].imshow(op_sobel, cmap=plt.cm.gray)
ax[1].set_title('Operador de Sobel')

ax[2].imshow(op_scharr, cmap=plt.cm.gray)
ax[2].set_title('Operador de Scharr')

ax[3].imshow(op_prewitt, cmap=plt.cm.gray)
ax[3].set_title('Operador de Prewitt')

for a in ax:
    a.axis('off')

plt.tight_layout()
plt.show()