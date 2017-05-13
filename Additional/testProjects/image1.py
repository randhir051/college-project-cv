import cv2
import numpy as np
import matplotlib.pyplot as plt

#IMREAD_GRAYSCALE 0
#IMREAD_COLOR 1
#IMREAD_UNCHANGED -1
img = cv2.imread('cat.jpeg',cv2.IMREAD_GRAYSCALE)

plt.imshow(img,cmap='gray',interpolation='bicubic')
plt.show()

cv2.imshow('my cats<3',img)
cv2.waitKey(0)
cv2.destroyAllWindows()