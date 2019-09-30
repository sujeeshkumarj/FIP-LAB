import cv2
import numpy as np
# img = cv2.imread('C:/Users/SUJEESH/Downloads/parrot.jpg')
# print('1',img.shape)
# scaling
# height, width = img.shape[:2]
# res = cv2.resize(img,(1*width, 1*height), interpolation=cv2.INTER_CUBIC)
# res = cv2.resize(img, None, fx=.1, fy=.1, interpolation=cv2.INTER_CUBIC)
# print('2',dst.shape)
#translation
img1 = cv2.imread('C:/Users/SUJEESH/Downloads/parrot.jpg',0)
rows,cols= img1.shape
M = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(img1,M,(cols,rows))



cv2.imshow('img1',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
