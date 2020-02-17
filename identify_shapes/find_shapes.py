'''Class to select method to find shapes in gray image'''

# import the necessary packages
import os
import cv2

method = os.getenv('METHOD', 'cv2')

result = [0] *256
if method == 'cv2':
    from  classify_cv2 import Classsify
elif method == 'diego':
    from  classify_diego import Classsify

classsify = Classsify()
result =  classsify.run(result)
for index, color in enumerate(result):
    print (color)
    print (index)
    print ('--')
