# -*- coding: utf-8 -*-
"""
Created on Sat Sep 09 21:29:37 2017

@author: Airtat
"""

import cv2
import numpy as np
from skimage import measure
from imutils import contours
import imutils

def circles(name, image2):
    imgC=cv2.imread('1a.png')
    params = cv2.SimpleBlobDetector_Params()
    params.minDistBetweenBlobs=1
    params.filterByColor=True
    params.blobColor=255
    
    params.minThreshold = 0
    params.maxThreshold=1000
    
    params.filterByArea = True
    params.minArea =200
    params.maxArea=4000
   
    params.filterByCircularity = False
    params.minCircularity = 0.1
    params.filterByConvexity = False
    params.filterByInertia = False
    detector = cv2.SimpleBlobDetector_create(params)
   
    keypoints = detector.detect(image2)
    print keypoints[0].size
    print keypoints[1].size
    print keypoints[2].size

    
    im_with_keypoints = cv2.drawKeypoints(image2, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    # Show blobs
    cv2.imshow(name, im_with_keypoints)


def mincircles(name, image1):
# find the contours in the mask, then sort them from left to
# right
    imgC=cv2.imread('1a.png')
    cnts= cv2.findContours(image1.copy(), cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    cnts = contours.sort_contours(cnts)[0]
 
# loop over the contours
    for (i, c) in enumerate(cnts):
	# draw the bright spot on the im
        
        (x, y, w, h) = cv2.boundingRect(c)
        ((cX, cY), radius) = cv2.minEnclosingCircle(c)
        #if int(radius)<200 and int(radius)>1:
        #print str(i), int(radius)
        cv2.circle(image1, (int(cX), int(cY)), int(radius),(0, 0, 255), 1)
       # cv2.putText(image1, "#{}".format(i + 1), (x, y - 15),cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
 
# show the output image
    
    cv2.imshow(name, image1)
            




img = cv2.imread('1a.png',0)
imgC=cv2.imread('1a.png')
#img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#blur = cv2.GaussianBlur(img, (11, 11), 0)
#img = cv2.medianBlur(img,5)

cv2.imshow('colour', imgC)


#cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
range=[100,120,110,130,115]
range=[100,150]

for i in range:  
    thresh = cv2.threshold(img, i, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.erode(thresh, None, iterations=2)
    thresh = cv2.dilate(thresh, None, iterations=4)
    # perform a connected component analysis on the thresholded
# image, then initialize a mask to store only the "large"
# components
    #circles(str(i)+'before',thresh)    
    
    labels = measure.label(thresh, neighbors=8, background=0)
    mask = np.zeros(thresh.shape, dtype="uint8")
    for label in np.unique(labels):
        if label==0:
            continue
        
	# otherwise, construct the label mask and count the
	# number of pixels 
        labelMask = np.zeros(thresh.shape, dtype="uint8")
        
        labelMask[labels == label] = 255
        numPixels = cv2.countNonZero(labelMask)
        #cv2.imshow('labelMask'+str(label),labelMask)
	# if the number of pixels in the component is sufficiently
	# large, then add it to our mask of "large blobs"
       # if numPixels > 10:
        mask=cv2.add(mask, labelMask)

    #cv2.imshow(str(i)+'before',mask)
    #mincircles(str(i)+'afterMINI',mask)
    circles(str(i)+'after',mask)
#cv2.imshow('detected circlesErode',thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()