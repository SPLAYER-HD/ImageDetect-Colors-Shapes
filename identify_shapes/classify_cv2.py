'''Class to find shapes in gray image with cv2'''

# import the necessary packages
import argparse
import cv2

from collections import OrderedDict
from load_data import LoadData
from transform_image import TransformImage
from find_color import FindColor


class Classsify():
    ''' class to classify '''

    def run(self, result, shape):
        loadData = LoadData()
        image = loadData.load()
        colors = OrderedDict({
			"black": (0, 0, 0),
			"gray": (200, 200, 200),
			"white": (255, 255, 255)})
        for (i, (name, rgb)) in enumerate(colors.items()):

            transformImage = TransformImage()
            image_transformed = transformImage.transform(image, rgb[0], shape)
            gray = cv2.cvtColor(image_transformed, cv2.COLOR_BGR2GRAY)
            blurred = cv2.GaussianBlur(gray, (5, 5), 0)
            thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]            
            cnts, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            contours_ = sorted(cnts, key=cv2.contourArea, reverse=True)[:10]
            contours = [cv2.approxPolyDP(cnt, 3, True) for cnt in cnts]

            findColor = FindColor()
            amount = findColor.run(image_transformed, cnts, gray, rgb[0])
            result[rgb[0]] = amount
        return result
