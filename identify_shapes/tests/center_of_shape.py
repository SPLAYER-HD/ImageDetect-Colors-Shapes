# import the necessary packages

import argparse
import imutils
import cv2
from PIL import Image
import numpy as np
from random import randint
 

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to the input image")
args = vars(ap.parse_args())
print ('cv2.__version__')
print (cv2.__version__)
# load the image, convert it to grayscale, blur it slightly,
# and threshold it
image = cv2.imread(args["image"])
img = Image.open(args["image"])
array = np.array(img)



gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
invimg = Image.fromarray(gray)
invimg.save('shades-of-grey_gray.png')
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
invimg = Image.fromarray(blurred)
invimg.save('shades-of-grey_blurred.png')
thresh = cv2.threshold(gray, 60, 80, cv2.THRESH_BINARY_INV)[1]
invimg = Image.fromarray(thresh)
invimg.save('shades-of-grey_thresh.png')

# find contours in the thresholded image
(cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#(_, cnts, _) = imutils.grab_contours(cnts)
print('cnts')
print(len(cnts))
print(len(cnts[0]))
#cv2.drawContours(image, cnts, -1, (240, 0, 159), 3)
#cv2.imshow("Image", image)
#cv2.waitKey(0)
for c in cnts:
    	# compute the center of the contour
	M = cv2.moments(c)
	print('M')
	#print(M)
	cX = int(M["m10"] / M["m00"])
	cY = int(M["m01"] / M["m00"])
	# draw the contour and center of the shape on the image
	cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
	cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
	cv2.putText(image, "center", (cX - 20, cY - 20),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
 
	# show the image
	#cv2.imshow("Image", image)
	#cv2.waitKey(0)

#invimg = Image.fromarray(dst)
#invimg.save('shades-of-grey_border.png')
#image = cv2.imread("shades-of-grey_border.png")
#img = Image.open('shades-of-grey_border.png')
array = np.array(img)
'''
for row_index, line in enumerate(array):
    #print (line)
    for column_index, pixel in enumerate(line):
        if(pixel[0] ==200):
            array[row_index][column_index]=[0, 0, 0]
            #21, 214, 234
'''

for row_index, line in enumerate(array):
    #print (line)
    for column_index, pixel in enumerate(line):
        if(pixel[0] ==255):
            array[row_index][column_index]=[21, 214, 234]

for row_index, line in enumerate(array):
    #print (line)
    for column_index, pixel in enumerate(line):
        if((row_index ==0 or row_index == len(array)-1)and (column_index == 1 or len(array[0])-1)):
            #print('entro0')
            array[row_index][column_index]=[255, 255, 255]
        if((row_index ==0 or row_index == len(array)-1)and (column_index == 0 or len(array[0])-1)):
            #print('entro')
            array[row_index][column_index]=[255, 255, 255]
        if((row_index ==1 or row_index == len(array)-2) and (column_index == 1 or len(array[0])-2)):
            #print('entro2')
            array[row_index][column_index]=[255, 255, 255]
        if(row_index == len(array)-3 and  len(array[0])-3):
            #print('entro3')
            array[row_index][column_index]=[255, 255, 255]


invimg = Image.fromarray(array)
invimg.save('shades-of-grey_red.png')
image = cv2.imread('shades-of-grey_red.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
invimg.save('shades-of-grey_gray.png')
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
invimg = Image.fromarray(blurred)
invimg.save('shades-of-grey_blurred.png')
##################444
'''
thresh = cv2.threshold(gray, 60, 80, cv2.THRESH_BINARY_INV)[1]
invimg = Image.fromarray(thresh)
invimg.save('shades-of-grey_thresh.png')

# find contours in the thresholded image
(cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#(_, cnts, _) = imutils.grab_contours(cnts)
print('cnts')
print(len(cnts))
print(len(cnts[0]))
#cv2.drawContours(image, cnts, -1, (240, 0, 159), 3)
#cv2.imshow("Image", image)
#cv2.waitKey(0)
for c in cnts:
    	# compute the center of the contour
	M = cv2.moments(c)
	print('M')
	#print(M)
	cX = int(M["m10"] / M["m00"])
	cY = int(M["m01"] / M["m00"])
	# draw the contour and center of the shape on the image
	cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
	cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
	cv2.putText(image, "center", (cX - 20, cY - 20),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
 
	# show the image
	cv2.imshow("Image", image)
	cv2.waitKey(0)
'''
######################444
thresh = cv2.threshold(gray, 210, 255, cv2.RETR_FLOODFILL)[1]
invimg = Image.fromarray(thresh)
invimg.save('shades-of-grey_thresh.png')



# find contours in the thresholded image
(cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
#(_, cnts, _) = imutils.grab_contours(cnts)
print('cnts')
print(len(cnts))
#print(len(cnts[0]))
#print(cnts)
#cv2.drawContours(image, cnts, -1, (240, 0, 159), 3)
#cv2.imshow("Image", image)
#cv2.waitKey(0)
print(len(cnts))
#print(len(cnts[0]))
# loop over the contours
for c in cnts:
	# compute the center of the contour
	M = cv2.moments(c)
	print('M')
	#print(M)
	cX = int(M["m10"] / M["m00"])
	cY = int(M["m01"] / M["m00"])
	# draw the contour and center of the shape on the image
	cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
	cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
	cv2.putText(image, "center", (cX - 20, cY - 20),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
 
	# show the image
	cv2.imshow("Image", image)
	cv2.waitKey(0)

####################################
thresh = cv2.threshold(gray, 255, 0, cv2.THRESH_TRUNC)[1]
invimg = Image.fromarray(thresh)
invimg.save('shades-of-grey_thresh.png')



# find contours in the thresholded image
(cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
#(_, cnts, _) = imutils.grab_contours(cnts)
print('cnts')
print(len(cnts))
#print(len(cnts[0]))
#print(cnts)
#cv2.drawContours(image, cnts, -1, (240, 0, 159), 3)
#cv2.imshow("Image", image)
#cv2.waitKey(0)
print(len(cnts))
#print(len(cnts[0]))
# loop over the contours
for c in cnts:
	# compute the center of the contour
	M = cv2.moments(c)
	print('M')
	#print(M)
	cX = int(M["m10"] / M["m00"])
	cY = int(M["m01"] / M["m00"])
	# draw the contour and center of the shape on the image
	cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
	cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
	cv2.putText(image, "center", (cX - 20, cY - 20),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
 
	# show the image
	cv2.imshow("Image", image)
	cv2.waitKey(0)
