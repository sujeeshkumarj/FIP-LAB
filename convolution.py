import cv2
import numpy as np

img=cv2.imread('C:/Users/SUJEESH/Downloads/friends.jpeg',0)

(d1,d2)=img.shape
print(d1,d2)

l = 3
q = 1

mask = np.ones((l,q,3), np.uint8)

for i in range(0,l):
    for j in range(0,q):
        mask[i,j] = 1

n1 = d1+3-1
n2 = d2+1-1

otpt = np.ones((n1,n2,3), np.uint8)

w1 = 'input'
w2 = 'output'

cv2.namedWindow(w1,cv2.WINDOW_FREERATIO)
cv2.resizeWindow(w1,400,400)
cv2.moveWindow(w1,0,0)

cv2.namedWindow(w2,cv2.WINDOW_FREERATIO)
cv2.resizeWindow(w2,400,400)
cv2.moveWindow(w2,0,400)

for i in range(0,n1):
    for j in range(0,n2):
        s = 0
        for m in range(0,l):
            if((i-m)>=0 and (i-m)<d1):
                for n in range(0,q):
                    if((j-n)>=0 and (j-n)<d2):

                     s = s + mask[m, n] * img[i-m, j-n]
        otpt[i,j] = s



cv2.imshow(w1,img)
cv2.imshow(w2,otpt)
cv2.waitKey(0)
cv2.destroyAllWindows()



