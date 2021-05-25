import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
#print(img)
#img[:]= 255,0,0  #[:]整体全为蓝色，加上指定范围[200:300,100:400]则指定长宽范围为蓝色
# start point, end point(这调用shape，注意先高度后宽度), color, thickness
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)
cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), 2)
# cv2.rectangle(img, (0, 0), (250, 350), cv2.FILLED) # 直接填充代替厚度
# start point, radius半径, color, thickness
cv2.circle(img, (400, 50), 30, (255, 255, 0), 5)
# front 字体, scale比例, color, thickness
cv2.putText(img, " OPENCV  ", (300, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 3)

cv2.imshow("Image", img)

cv2.waitKey(0)