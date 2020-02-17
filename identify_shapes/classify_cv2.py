'''Class to find shapes in gray image with cv2'''

# import the necessary packages
import argparse
import cv2
import numpy as np

from load_data import LoadData
from transform_image import TransformImage


class Classsify():
    ''' class to classify '''

    def run(self, result):
        print ('Running cv2 algorithm')
        loadData = LoadData()
        image = loadData.load()
        transformImage = TransformImage()
        edges = transformImage.transform(image)

        cnts, hierarchy = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(cnts, key=cv2.contourArea, reverse=True)[:10]

        for c in contours:
            x = ((c[0])[0])[0]
            y = ((c[0])[0])[1]

            color_index = (image[x][y])[0]
            result[color_index] += 1
            #cv2.drawContours(image, [c], 0, (100), 5)

        # show the image
        #cv2.imshow("Image", image)    
        #cv2.waitKey(0)
        return result
