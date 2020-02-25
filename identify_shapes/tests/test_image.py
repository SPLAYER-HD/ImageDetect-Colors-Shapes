"""from skimage import io
import skimage
import os
filename = os.path.join(skimage.data_dir, '/home/splayer/Downloads/shades-of-grey2.png')
camera = io.imread(filename)
"""
import numpy as np
from PIL import Image

img = Image.open('/home/splayer/Downloads/shades-of-grey.png')
img.thumbnail((256,256))

array = np.array(img)
array.setflags(write=True)

#array[0][0] = [0,0,0]
#array[0][255] = [0,0,0]
print(str(array[0][0]))  

#euclidean distance 
dist = (array[0] - array[1])**2
dist = np.sum(dist, axis=1)
dist = np.sqrt(dist)
print (dist)

with open("output.txt", "w") as txt_file:
    for line in array:
        #print (line)
        txt_file.write(" ".join(str(line)) + "\n")



invimg = Image.fromarray(array)
invimg.save('shades-of-grey.png')