import cv2
# Cascade 小瀑布，瀑布状物；串联
faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
img = cv2.imread('Resources/lena.png')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)  #scale 1.1 最小邻居
# 创建边界框，颜色，厚度
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow("Result", img)
cv2.waitKey(0)