'''Class to find image and load it'''

# import the necessary packages
import os
import cv2
import numpy as np

class LoadData():
    def load(self):
        image_path = 'resources/'+os.getenv('IMAGE', 'sample.bin')
        xbash = np.fromfile(image_path, dtype='uint8')
        image_path = 'image.png'
        cv2.imwrite(image_path, xbash[:65536].reshape(256,256))
        return image_path
