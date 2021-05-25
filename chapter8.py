import cv2
import numpy as np

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

def getContours(img):
    # 找到这个image外部的轮廓，层级，对应第二个参数是retrieval method检索方式（这里用external其他方式直接filter out）
    # 第三个参数 approximation 可以request compressed value (reduce points) 或者all information (none这里提取所有轮廓不压缩)
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        # print(area)
        if area > 500:
            # 以下是根据轮廓获取曲线，再根据曲线获取折线，再根据折线获取拐点，根据拐点数就是角度
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            # calculate perimeter = the curve length which is
            peri = cv2.arcLength(cnt, True)
            # print(peri)
            # the second argument is resolution for the length arc弧线; the third will get true when there is
            # not getting a result for the solution (result) 这里假设图形都是close封闭的，这里对边界采样是为了取拐点数

            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)  # 这里是approx是get the points of the corner points
            # print(len(approx))
            # 这里取length就可以知道有几个拐点，那么就可以进行图形分类，categories
            objCor = len(approx)
            # 这里detect bounding box 找边界 w这里是width h这里是 height
            x, y, w, h = cv2.boundingRect(approx)
            # 外边界框3个拐点是triangle
            if objCor ==3: objectType ="Tri"
            elif objCor == 4:
                # 利用长宽比判断是否为矩形还是长方形 aspect rate
                aspRatio = w/float(h)
                if aspRatio >0.98 and aspRatio <1.03:
                    objectType= "Square"
                else:
                    objectType = "Rectangle"
            elif objCor > 4:
                objectType = "Circles"
            else:
                objectType = "None"

            cv2.rectangle(imgContour, (x, y), (x+w, y+h), (0, 255, 0), 2)
            # 第三个参数是找中心点，第四个是字体，第五个 scale， color，最后一个是font scale 字体大小
            cv2.putText(imgContour, objectType,
                        (x+(w//2)-10, y+(h//2)-10), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                        (0, 0, 0), 2)




path = 'Resources/shapes.png'
img = cv2.imread(path)
imgContour = img.copy()

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
# canny 精明的，谨慎的；节约的
imgCanny = cv2.Canny(imgBlur, 50, 50)
getContours(imgCanny)
# 用blank补足缺损区域
imgBlank = np.zeros_like(img)
# 设置两行，注意这个blank是为了补上缺损
imgStack = stackImages(0.8, ([img, imgGray, imgBlur], [imgCanny, imgContour, imgBlank]))

cv2.imshow("Stack", imgStack)
cv2.waitKey(0)
