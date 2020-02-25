'''Class to find shapes in gray image with cv2'''

# import the necessary packages
import argparse
import cv2
import numpy as np
from scipy.spatial import distance as dist

from load_data import LoadData
from transform_image import TransformImage


class FindColor():
    ''' class to classify '''

    def run(self, image, cnts, gray, color):
        mask = np.zeros(gray.shape,np.uint8)
        amount = 0
        
        for c in cnts:
            mask = np.zeros(image.shape[:2], dtype="uint8")
            cv2.drawContours(mask, [c], -1, 255, -1)
            mask = cv2.erode(mask, None, iterations=2)
            mean = cv2.mean(image, mask=mask)[:3]
            minDist = (np.inf, None)
            for i in [0,255]:
                d = dist.euclidean(i, mean)
                if d < minDist[0]:
                    minDist = (d, i)
            if color == 200:
                if minDist[1] == 0:
                    amount += 1
            elif minDist[1] == color:
                amount += 1

            ## draw contours
            '''
            M = cv2.moments(c)
            d = M["m00"]
            if d <= 0:
                d =1
            cX = int(M["m10"] / d)
            cY = int(M["m01"] / d)
            cv2.circle(image, (cX, cY), 7, (255, 0, 0), -1)
            cv2.putText(image, "center", (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
            cv2.drawContours(image, [c], 0, (100), 5)
            cv2.imshow("Image find color = "+str(color), image)    
            cv2.waitKey(0)
            '''
        return amount
