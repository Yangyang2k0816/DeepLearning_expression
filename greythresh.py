#coding:utf8
import cv2
import matplotlib.pyplot as plt
import numpy as np
import sys
import os

filename="./1 depth_of_field_food.jpg" #柿子彩色图

img = cv2.imread(filename)
grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
grey = cv2.resize(grey,(600,400))

##--------经验阈值法--------##
plt.figure(figsize=(12,6))
plt.subplot(221)
plt.imshow(grey,cmap ='gray')
plt.title("original gray pic")

img50 = np.array(grey)
img50[img50<50]=0
plt.subplot(222)
plt.imshow(img50, cmap="gray")
plt.title("threshold set to 50")

img100 = np.array(grey)
img100[img100<100]=0
plt.subplot(223)
plt.imshow(img100, cmap="gray")
plt.title("threshold set to 100")

img150 = np.array(grey)
img150[img150<150]=0
plt.subplot(224)
plt.imshow(img150, cmap="gray")
plt.title("threshold set to 150")

plt.tight_layout()
plt.show()

##------Otsu阈值法------##
greyblur = cv2.GaussianBlur(grey,(5,5),0)
th,result = cv2.threshold(greyblur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
print (th)
plt.figure(figsize=(12,6))
plt.subplot(121)
plt.imshow(grey,cmap ='gray')
plt.title("original gray pic")
plt.subplot(122)
plt.imshow(result, cmap="gray")
plt.title("otsu threshold")
plt.show()

##------转换空间再求阈值------##
rgbimg = cv2.imread(filename)
rgbimg = cv2.resize(rgbimg,(600,400))
hsvimg = cv2.cvtColor(rgbimg,cv2.COLOR_BGR2HSV)
plt.figure(figsize=(12,6))
plt.subplot(131)
plt.imshow(hsvimg[:,:,0],cmap ='gray')
plt.title("h")
plt.subplot(132)
plt.imshow(hsvimg[:,:,1],cmap ='gray')
plt.title("s")
plt.subplot(133)
plt.imshow(hsvimg[:,:,2],cmap ='gray')
plt.title("v")
plt.show()

grey = hsvimg[:,:,2]
greyblur = cv2.GaussianBlur(grey,(5,5),0)
th,result = cv2.threshold(greyblur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
print (th)
plt.figure(figsize=(12,6))
plt.subplot(121)
plt.imshow(grey,cmap ='gray')
plt.title("original gray pic")
plt.subplot(122)
plt.imshow(result, cmap="gray")
plt.title("otsu threshold")
plt.show()
