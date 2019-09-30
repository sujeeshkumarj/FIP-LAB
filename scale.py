import cv2
img = cv2.imread('C:/Users/SUJEESH/Downloads/friends.jpeg',0)
img1 = cv2.imread('C:/Users/SUJEESH/Downloads/friends.jpeg',0)
(dim1,dim2) = img1.shape
print(dim1, dim2)
win1 = "input image"
win2 = "output image"

cv2.namedWindow(win1,cv2.WINDOW_NORMAL)
cv2.resizeWindow(win1,400,400)
cv2.moveWindow(win1,50,0)

cv2.namedWindow(win2,cv2.WINDOW_NORMAL)
cv2.resizeWindow(win2,400,400)
cv2.moveWindow(win2,50,400)
print(type(dim1))

px = float(input('enter the x value of pivot:'))
py = float(input('enter the y value of pivot:'))
sx = float(input('enter scaling factor for x :'))
sy = float(input('enter scaling factor for y :'))

for i in range (0,dim1):
    for j in range (0,dim2):
        img1[i,j]=0

for i in range (0,dim1):
    snx=int(((i-px)*sx)+px)
    for j in range (0,dim2):
        sny=int(((j-py)*sy)+py)
        if(snx<dim1 and sny<dim2):
            if(snx>=0 and sny>=0):
                img1[snx,sny] = img[i,j]

print(type(i))
cv2.imshow(win1, img)
cv2.imshow(win2, img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
