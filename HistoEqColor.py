# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 11:35:04 2019

@author: eagle
source: opencv.org
"""
import cv2
import numpy as np
import argparse

# run this code using the command prompt
parser = argparse.ArgumentParser(description='Code for Histogram Equalization tutorial.')
parser.add_argument('--input', help='Path to input image.', default='orig_color_img_2.jpg')  # loading the image
                                                                                          # when running this code in command, put --input orig_gray_img_2.jpg
                                                                                          # after python HistoEqOpenCV.py to run it on that image
args = parser.parse_args()
src = cv2.imread(args.input)

# if no image is loaded
if src is None:
    print('Could not open or find the image:', args.input)
    exit(0)

img_yuv = cv2.cvtColor(src, cv2.COLOR_BGR2YUV)

# equalize the histogram of the Y channel
img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])

# convert the YUV image back to RGB format
img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

height, width = src.shape[:2]
height2, width2 = img_output.shape[:2]

if height > 800 or width > 800:
    src = cv2.resize(src, (int(width/1.5), int(height/1.5)), interpolation = cv2.INTER_CUBIC)

if height2 > 800 or width2 > 800:
    img_output = cv2.resize(img_output, (int(width/1.5), int(height/1.5)), interpolation = cv2.INTER_CUBIC)

cv2.imshow('Color input image', src)
cv2.imshow('Histogram equalized', img_output)
cv2.waitKey()