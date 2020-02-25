# import the necessary packages
import argparse
import cv2
import numpy as np
from PIL import Image

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="/home/splayer/Downloads/shades-of-grey2.png")
args = vars(ap.parse_args())
 
# load the image, convert it to grayscale, blur it slightly,
# and threshold it
image = cv2.imread(args["image"], cv2.IMREAD_GRAYSCALE)
#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#blurred = cv2.GaussianBlur(gray, (5, 5), 0)
_, thresh = cv2.threshold(image, 245, 255, cv2.THRESH_BINARY)


cnts, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
#cnts = imutils.grab_contours(cnts)

#cnts = cnts[0] if len(cnts) == 2 else cnts[1]
#cv2.imshow("Image", image)
#cv2.waitKey(0)

for c in cnts:
    # compute the center of the contour
    cv2.drawContours(image, [c], 0, (100), 5)
    print('-------')
# show the image
cv2.imshow("Image", image)    
cv2.waitKey(0)



####
array = np.array(Image.open(args["image"]))
for row_index, line in enumerate(array):
    #print (line)
    for column_index, pixel in enumerate(line):
        #print (pixel)
        if(pixel[0] ==200):
            array[row_index][column_index]=[255, 255, 255]
print ('eeeee')
x =(((cnts[0])[0])[0])[0]
y = (((cnts[0])[0])[0])[1]
print(x)
print(y)
print ('eeeee')
print (array[x][y])
print ('eeeee')

print ('eeeee')
x =(((cnts[0])[0])[0])[0]
y = (((cnts[0])[0])[0])[1]
print(x)
print(y)
print ('eeeee')
print (array[x][y])
print ('eeeee')
invimg = Image.fromarray(array)
invimg.save('test.png')
image = cv2.imread('test.png', cv2.IMREAD_GRAYSCALE)
_, thresh = cv2.threshold(image, 245, 255, cv2.THRESH_BINARY)
cnts, _ = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


for c in cnts:
    # compute the center of the contour
    print('-------')
    cv2.drawContours(image, [c], 0, (100), 5)

# show the image
cv2.imshow("Image", image)    
cv2.waitKey(0)
