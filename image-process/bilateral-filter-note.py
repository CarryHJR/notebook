#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-28T06:52:38.406Z
# @Author  : CarryHJR

import cv2
import numpy as np

def nothing(x):
    pass


img = cv2.imread('pictures/证件照.jpg')
# print(img)
cv2.namedWindow("real")
cv2.imshow("real", img)
cv2.namedWindow("Image")




cv2.createTrackbar('thres1', 'Image', 30, 255, nothing)
cv2.createTrackbar('thres2', 'Image', 200, 255, nothing)
cv2.createTrackbar('size', 'Image', 50, 255, nothing)
cv2.createTrackbar('sigmaColor', 'Image', 21, 255, nothing)
cv2.createTrackbar('sigmaSpace', 'Image', 21, 255, nothing)
cv2.createTrackbar('saturation', 'Image', 50, 255, nothing)


def add_s(img, value):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #convert it to hsv
    # hsv[:,:,2] += value
    h, s, v = cv2.split(hsv)
    # value = 20
    v_before = v.copy()
    s[s>(255-value)]=255
    s[s<=(255-value)]+=value
    # s[:,:]+=20
    # v[v<value]=0
    # v[v>=value] -=value
    final_hsv = cv2.merge((h, s, v))
    img_add_s = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img_add_s

# img = add_s(img, 20)

while True:
    size = cv2.getTrackbarPos('size', 'Image')
    sigmaColor = cv2.getTrackbarPos('sigmaColor', 'Image')
    sigmaSpace = cv2.getTrackbarPos('sigmaSpace', 'Image')

    img_filter = cv2.bilateralFilter(img,size,sigmaColor,sigmaSpace)

    thres1 = cv2.getTrackbarPos('thres', 'Image')
    thres2 = cv2.getTrackbarPos('thres2', 'Image')

    canny = cv2.Canny(img, thres1, thres2)
    mask = np.array([canny,canny,canny]).transpose(1,2,0)
    img_canny = img*(1-mask/255)
    cv2.imshow("mask", (255-mask))

    value = cv2.getTrackbarPos('saturation', 'Image')
    
    img_s = add_s(img_canny,value)
    cv2.imshow("Image", img_s)
    

    # img = cv2.threshold(blurred, thresh, 255, cv2.THRESH_BINARY_INV)[1]
    # 键盘检测函数，0xFF是因为64位机器
    # https: // stackoverflow.com / questions / 20539497 / opencv - python - waitkey d- dont - respond
    k = cv2.waitKey(1) & 0xFF
    # print k
    if k == ord('q'):
        break


cv2.destroyAllWindows()
