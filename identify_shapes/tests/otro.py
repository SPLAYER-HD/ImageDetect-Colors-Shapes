# import the necessary packages
import argparse
import cv2
import numpy as np
from PIL import Image

result = [0] *256
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="/home/splayer/Downloads/shades-of-grey2.png")
args = vars(ap.parse_args())
 
# load the image, convert it to grayscale, blur it slightly,
# and threshold it
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5,5), 0)
edges = cv2.Canny(gray, 60, 0)
cnts, hierarchy = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(cnts, key=cv2.contourArea, reverse=True)[:10]

array = np.array(Image.open(args["image"]))
for c in contours:
    # compute the center of the contour
    x = ((c[0])[0])[0]
    y = ((c[0])[0])[1]
    print('-------'+str(x))
    print('-------'+str(y))
    color_index = (array[x][y])[0]
    print('---color'+str(color_index))
    result[color_index] += 1
    cv2.drawContours(image, [c], 0, (100), 5)

# show the image
cv2.imshow("Image", image)    
cv2.waitKey(0)
print (result)
