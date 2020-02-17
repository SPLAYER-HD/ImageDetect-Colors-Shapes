'''Class to find image and load it'''

# import the necessary packages
import os
import cv2

class LoadData():
    def load(self):
        image_path = '/resources/'+os.getenv('IMAGE', 'shades-of-grey.png')
        # load the image, convert it to grayscale, blur it slightly,
        # and threshold it
        image = cv2.imread(image_path)
        return image