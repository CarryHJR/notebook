#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-28T06:52:38.406Z
# @Author  : CarryHJR

import cv2
import numpy as np

def nothing(x):
    pass


img = cv2.imread('pictures/images.jpeg')
cv2.namedWindow("real")
cv2.imshow("real", img)
cv2.namedWindow("Image")


cv2.createTrackbar('thres1', 'Image', 30, 255, nothing)
cv2.createTrackbar('thres2', 'Image', 100, 255, nothing)

while True:
    
    thres1 = cv2.getTrackbarPos('thres', 'Image')
    thres2 = cv2.getTrackbarPos('thres2', 'Image')

    canny = cv2.Canny(img, thres1, thres2)
    mask = np.array([canny,canny,canny]).transpose(1,2,0)
    img_canny = img*(1-mask/255)
    cv2.imshow("mask", (255-mask))
    cv2.imshow("Image", img_canny)

    # img = cv2.threshold(blurred, thresh, 255, cv2.THRESH_BINARY_INV)[1]
    # 键盘检测函数，0xFF是因为64位机器
    # https: // stackoverflow.com / questions / 20539497 / opencv - python - waitkey d- dont - respond
    k = cv2.waitKey(1) & 0xFF
    # print k
    if k == ord('q'):
        break


cv2.destroyAllWindows()
