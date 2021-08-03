# -*- encoding: utf-8 -*-
import time
import os
import cv2
import sys

capin = cv2.VideoCapture("./opencv.mov") #读取视频
fps =int(capin.get(cv2.CAP_PROP_FPS)) #获得帧率
# 获得视频大小
if capin.isOpened(): 
    width  = capin.get(cv2.CAP_PROP_FRAME_WIDTH)  
    height = capin.get(cv2.CAP_PROP_FRAME_HEIGHT)
    print("原始视频大小："+str(width)+"*"+str(height))

# 计算新尺寸
neww = 720
newh = int(neww*height/width)

videoout = cv2.VideoWriter("./", cv2.VideoWriter_fourcc('I', '4', '2', '0'), fps, (neww,newh))

cv2.namedWindow("im",0)

# 通过摄像头的方式
while True:
    t1 = time.time()
    ret, frame = capin.read()  # ret是bool型，当读完最后一帧就是False，frame是ndarray型
    if ret == False:  #
        break

    cv2.imshow("im",frame)
    newframe = cv2.resize(frame,(neww,newh))
    videoout.write(newframe)

    k = cv2.waitKey(10)
    if k == ord('q'):  # 检测到按下q，就break，waitKey(10)相当于10ms延时
         break

capin.release()
cv2.destroyAllWindows()

