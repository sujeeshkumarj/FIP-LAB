import cv2
import math
import numpy as np
img0 = cv2.imread('C:/Users/SUJEESH/Downloads/friends.jpeg',cv2.IMREAD_GRAYSCALE)
# img1 = cv2.imread('C:/Users/SUJEESH/Downloads/friends.jpeg',cv2.IMREAD_GRAYSCALE)

(d2, d1) = img0.shape
print(d1,d2)

img1 = np.zeros((d1,d2,3), np.uint8)
otpt = np.zeros((d1,d2,3), np.uint8)
img2 = np.zeros((d1,d2,3), np.uint8)

w1 = 'input'
w2 = 'output'
w3 = 'interpolated output'

cv2.namedWindow(w1,cv2.WINDOW_FREERATIO)
cv2.resizeWindow(w1,400,400)
cv2.moveWindow(w1,0,0)

cv2.namedWindow(w2,cv2.WINDOW_FREERATIO)
cv2.resizeWindow(w2,400,400)
cv2.moveWindow(w2,0,400)

cv2.namedWindow(w3,cv2.WINDOW_FREERATIO)
cv2.resizeWindow(w3,400,400)
cv2.moveWindow(w3,400,0)

print(type(d1))

xr = int(input('enter the x value of pivot:'))
yr = int(input('enter the y value of pivot:'))
ang = int(input('enter the angle :'))

for i in range (0 ,d2):
    for j in range (0, d1):
        img1[i,j] = 0

for i in range (0, d2):
    # print(i,ssx)
    for j in range (0, d1):
        xxr = int(xr+((j-xr)*math.cos(ang*(math.pi/180)))-(((i)-yr)*math.sin(ang*(math.pi/180))))
        yyr = int(yr+((j-xr)*math.sin(ang*(math.pi/180)))+(((i)-yr)*math.cos(ang*(math.pi/180))))
        # print("x=", j, "x'=", xxr, "y=", i," y'=", yyr)
        if (yyr<d2 and xxr<d1):
            if(yyr>=0 and xxr>=0):
                img1[d2-yyr-1, xxr] = img0[d2-i-1, j]


# interpolate rotate

for i in range (0 ,d1):
    for j in range (0, d2):
        otpt[i,j] = img1[i,j]
print(img1[0,0])
print(otpt[0,0])
for y in range (d1-2, 1, -1):
    for x in range (d2-2, 1, -1):
        # print('hi')
        if(img1[y,x,0]== 0 and img1[y,x,1]==0 and img1[y,x,2]==0):
            f = (int(img1[y+1, x-1, 0])+int(img1[y+1, x+1, 0])+int(img1[y-1, x-1, 0])+int(img1[y-1, x+1, 0]))/4
            otpt[y, x, 0] = f
            otpt[y, x, 1] = f
            otpt[y, x, 2] = f

cv2.imshow(w1,img0)
cv2.imshow(w2,img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
