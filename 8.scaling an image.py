import cv2
img = cv2.imread("E:/Computer Vision/computer vision input and output/1.grayscaleinput.png")
cv2.imshow("original image",img)
cv2.waitKey(0)
img = cv2.resize(img,(600,600))
cv2.imshow("image",img)
cv2.waitKey(0)
img = cv2.resize(img,(100,100))
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


