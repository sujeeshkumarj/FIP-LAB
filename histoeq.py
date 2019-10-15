import cv2
import numpy as np
img = cv2.imread('C:/Users/SUJEESH/Downloads/friends.jpeg',cv2.IMREAD_GRAYSCALE)


(d1, d2) = img.shape
print(d1,d2)
otpt = np.zeros((d1,d2,1), np.uint8)

r = np.zeros(256)
p = np.zeros(256)
s = np.zeros(256)

w1 = 'input'
w2 = 'output'

cv2.namedWindow(w1,cv2.WINDOW_KEEPRATIO)
cv2.resizeWindow(w1,400,400)
cv2.moveWindow(w1,0,0)

cv2.namedWindow(w2,cv2.WINDOW_KEEPRATIO)
cv2.resizeWindow(w2,400,400)
cv2.moveWindow(w2,0,400)

print(type(d1))


for i in range (0, d1):
    for j in range (0, d2):
        temp = img[i,j]
        r[temp]= r[temp]+1



for i in range ( 0, 256):
    p[i] = r[i]/(d1 * d2)

for i in range (0, 256):
    temp = 0
    for j in range (0, i+1):
        temp = temp + p[j]
    s[i] = int(199 * temp)

for i in range (0, d1):
    for j in range (0, d2):
        temp = img[i,j]
        otpt[i,j] = s[temp]

for i in range(0, 256):
    print(i,"| r=",r[i]," p=",p[i]," s[",i,"]=",s[i])

print(type(i))
cv2.imshow(w1,img)
cv2.imshow(w2,otpt)
cv2.waitKey(0)
cv2.destroyAllWindows()
