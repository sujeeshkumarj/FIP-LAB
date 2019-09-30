import cv2
image1 = cv2.imread('C:/Users/SUJEESH/Downloads/test.png',cv2.IMREAD_GRAYSCALE)
image0 = cv2.imread('C:/Users/SUJEESH/Downloads/test.png')

# cv2.imshow('suji',image1)

firstwindow = "input image"
secondwindow = "output image"

cv2.namedWindow(firstwindow,cv2.WINDOW_NORMAL)
cv2.resizeWindow(firstwindow,400,400)
cv2.moveWindow(firstwindow,50,0)

cv2.namedWindow(secondwindow,cv2.WINDOW_NORMAL)
cv2.resizeWindow(secondwindow,400,400)
cv2.moveWindow(secondwindow,100,400)

# px = image1[25,25]
# print(px)
(dim1,dim2, dim3) = image0.shape
print('rows =',dim1)
print('columns =',dim2)
print('d3',dim3)
print(image0[0,20])

for i in range (0,dim1):

        for j in range (0,dim2):

            if(image1[i,j]>180 and image1[i, j]<245 ):
              image0[i, j] = [255, 0, 0]
             # image0[i, j] = image1[i, j] - (10, 10, 10)
            elif(image1[i,j]<90 ):

             image0[i, j] = [0, 0, 255]
            elif (image1[i, j]<245):

             image0[i, j] = [0, 255, 0]


cv2.imshow(firstwindow,image1)
cv2.imshow(secondwindow,image0)

cv2.waitKey(10000)
cv2.destroyAllWindows()
