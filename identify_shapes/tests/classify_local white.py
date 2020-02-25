'''Class to find shapes in gray image with cv2'''

# import the necessary packages
import argparse
import cv2 as cv2
import os
import numpy as np
from PIL import Image

from load_data import LoadData
from transform_image import TransformImage

result = [0] *256
image_path = '../resources/'+os.getenv('IMAGE', 'sample.bin')
xbash = np.fromfile(image_path, dtype='uint8')
#print(xbash.shape)
image_path = 'image.png'
x = 256
y = 256
cv2.imwrite(image_path, xbash[:x*y].reshape(x,y))

# load the image, convert it to grayscale, blur it slightly,
# and threshold it
array = np.array(Image.open(image_path))
#print(array)
for row_index, line in enumerate(array):
    #print (line)
    for column_index, pixel in enumerate(line):
        #print (pixel)
        if(pixel ==200):
            array[row_index][column_index]='0'
        if(pixel ==0):
            array[row_index][column_index]='0'
invimg = Image.fromarray(array)
invimg.save(image_path)

image = cv2.imread(image_path)

####
row, col = image.shape[:2]
bottom = image[row-2:row, 0:col]
mean = cv2.mean(bottom)[0]

bordersize = 10
border = cv2.copyMakeBorder(
    image,
    top=bordersize,
    bottom=bordersize,
    left=bordersize,
    right=bordersize,
    borderType=cv2.BORDER_CONSTANT,
    value=[0, 0, 0]
)

image = border

###
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow("Gray", gray)    
#cv2.waitKey(0)

#gray = cv2.GaussianBlur(gray, (5,5), 0)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
#cv2.imshow("Blurred", blurred)    
#cv2.waitKey(0)

edges = cv2.Canny(gray, 60, 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

cv2.imshow("Imageb", blurred)    
cv2.waitKey(0)

cnts, hierarchy = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours_ = sorted(cnts, key=cv2.contourArea, reverse=True)[:10]
contours = [cv2.approxPolyDP(cnt, 3, True) for cnt in cnts]

final = np.zeros(image.shape,np.uint8)
mask = np.zeros(gray.shape,np.uint8)

r =0 
for c in cnts:
    # average L*a*b* value for the masked region
    mask = np.zeros(image.shape[:2], dtype="uint8")
    cv2.drawContours(mask, [c], -1, 255, -1)
    mask = cv2.erode(mask, None, iterations=2)
    mean = cv2.mean(image, mask=mask)[:3]
    # initialize the minimum distance found thus far
    minDist = (np.inf, None)
    print ('//////////////')
    print(mean[0])
    print ('black' if mean[0]<15  else 'other')
    print ('--------------/////////////////////-------------')
    print ('//////////////')
    print ('Grey' if mean[0]<220 and mean[0]>180  else 'other')
    print ('--------------/////////////////////-------------')
    print ('//////////////')
    print ('white' if mean[0]<256 and mean[0]>130  else 'other')
    print ('--------------/////////////////////-------------')

    x = ((c[0])[0])[0]
    y = ((c[0])[0])[1]
    #print (str(c))
    M = cv2.moments(c)

    d = M["m00"]
    if d <= 0:
        d =1
    cX = int(M["m10"] / d)
    cY = int(M["m01"] / d)
    print(image[cX][cY])
    cv2.circle(image, (cX, cY), 7, (255, 0, 0), -1)
    cv2.putText(image, "center", (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
    print('==========================')
    #for p in c:
        #print(image[p[0][0]][p[0][1]])
    color_index = (image[x][y])[0]
    result[color_index] += 1
    print ('-------------------------')
    #print (image[x][y])
    #print (image[x][y])
    cv2.drawContours(image, [c], 0, (100), 5)
    # show the image
    cv2.imshow("Image"+str(r), image)    
    cv2.waitKey(0)

    r+=1
print (result)

