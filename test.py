import cv2
print(cv2.__version__)
image = cv2.imread("C:/Users/SUJEESH/Downloads/parrot.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Original image',image)
cv2.imshow('Gray image', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
