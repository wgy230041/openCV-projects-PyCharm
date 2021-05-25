######################## READ IMAGE ############################
# import cv2
# # print("package Imported")
# # LOAD AN IMAGE USING 'IMREAD'
# img = cv2.imread("Resources/lena.png")
# # DISPLAY
# cv2.imshow("Lena Soderberg",img)
# cv2.waitKey(0)
######################### READ VIDEO #############################
# import cv2
# frameWidth = 640
# frameHeight = 480
# cap = cv2.VideoCapture("Resources/test_video.mp4")
# while True:
#     success, img = cap.read()
#     img = cv2.resize(img, (frameWidth, frameHeight))
#     cv2.imshow("Result", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):  # waitkey返回按键对应ASCII值，0xFF（16进制数）按位与后8位（2进制是8个1），判断是为了避免其他按键干扰
#         break
######################### READ WEBCAM  ############################
import cv2
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)       # web camera id 默认是0
cap.set(3, frameWidth)          # id=3 在set里面是宽
cap.set(4, frameHeight)
cap.set(10, 150)                # id=10 是亮度
while True:
    success, img = cap.read()
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
