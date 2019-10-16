import cv2
import numpy as np

img= cv2.imread('C:/Users/SUJEESH/Downloads/friends.jpeg',0)

d1 ,d2 = img.shape

img1 =np.zeros((d1 ,d2),dtype = 'uint8')

min = 20
max = 90

for i in range(d1):
    for j in range(d2):
        if img[i,j]>min and img[i,j]<max:
            img1[i,j] = 255
        else:
            img1[i,j] = 0

cv2.imshow('intslice',img1)
cv2.waitKey(0)


