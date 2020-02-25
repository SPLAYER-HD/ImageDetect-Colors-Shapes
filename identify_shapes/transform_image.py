'''Class to transform image into a valid binary to find contours'''
# import the necessary packages
import cv2
import numpy as np
from PIL import Image

class TransformImage():
    def transform(self, image_path, color, shape):
        img = Image.open(image_path)
        array = np.array(img)
        #print(array)
        for row_index, line in enumerate(array):
            #print (line)
            for column_index, pixel in enumerate(line):
                #print (pixel)
                if(pixel ==200):
                    if color == 0:
                        array[row_index][column_index]='255'
                    elif color == 200 or color == 255:
                        array[row_index][column_index]='0'
                if(pixel ==0):
                    if color == 0:
                        array[row_index][column_index]='0'
                    elif color == 200:
                        array[row_index][column_index]='255'
        img.close()
        invimg = Image.fromarray(array)
        invimg.save('image'+str(color)+'.png')
        invimg.close()
        image = cv2.imread('image'+str(color)+'.png')

        if color == 255:
            value=[0, 0, 0]
        else:
            value=[255, 255, 255]

        bordersize = 10
        border = cv2.copyMakeBorder(
            image,
            top=bordersize,
            bottom=bordersize,
            left=bordersize,
            right=bordersize,
            borderType=cv2.BORDER_CONSTANT,
            value=value
        )
        image = border
        image = cv2.resize(image,(int(shape[0]),int(shape[1])))
        
        return image
