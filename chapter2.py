import cv2
import numpy as np

img = cv2.imread("Resources/lena.png")
kernel = np.ones((5, 5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0) #kernel size 只能用奇数
imgCanny = cv2.Canny(img, 50, 200) #edge detactor
# 有时候参数设置不好 图像edge识别会因为gap 或者join不合适造成 无法正确识别edge的情况，所以需要增加
#increase the thickness厚度，可以dilation 扩大,膨胀
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
#erosion 侵蚀，腐蚀
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)
