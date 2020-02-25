"""from skimage import io
import skimage
import os
filename = os.path.join(skimage.data_dir, '/home/splayer/Downloads/shades-of-grey2.png')
camera = io.imread(filename)
"""
import numpy as np
from PIL import Image



img = Image.open('/home/splayer/Downloads/shades-of-grey.png')
img.thumbnail((100,100))

array = np.array(img)
array.setflags(write=True)

#array[0][0] = [0,0,0]
array[0][1] = [1,255,255]
array[1][0] = [0,255,255]
#array[1][1] = [255,255,255]
#array[1][1] = [255,255,255]
#array[0][255] = [0,0,0]
#print(str(array[0][0]))

#euclidean distance 
'''dist = (array[0] - array[1])**2
dist = np.sum(dist, axis=1)
dist = np.sqrt(dist)
print (dist)
'''
color_continue=False
result = [0] *256
excluded_list = [[0,0]]
'''print ('array[0[0]  '+str(array[0][0]))
print ('excluded_list[0]  '+str(excluded_list[0]))
'''
def isPositive(value):
    return value-1 >0
def validateNeighbors(array, row_index, column_index, step, excluded_list):
    print ('Start Validate Neighbor')
    '''print ('row_index == '+str(row_index))
        print ('column_index == '+str(column_index))
        print ('array[row_index+1][column_index]  '+str(array[row_index+1][column_index]))
    '''
    print ('pixel  --- '+str(array[row_index][column_index][0]))
    color_continue=False
    #while (step <8):
    
    print('step '+str(step))
    near_cell = None
    if isPositive(row_index):
        if (array[row_index][column_index][0] ==  array[row_index-1][column_index][0]):
            print('array[row_index-1][column_index]' + str(array[row_index-1][column_index]))
            
        if (array[row_index][column_index][0] ==  array[row_index-1][column_index+1][0]):
            print('array[row_index-1][column_index-1]' + str(array[row_index-1][column_index+1]))
        if isPositive(column_index):
            if (array[row_index][column_index][0] ==  array[row_index-1][column_index-1][0]):
                print('array[row_index-1][column_index-1]' + str(array[row_index-1][column_index-1]))
    
    if isPositive(column_index):
        if (array[row_index][column_index][0] ==  array[row_index][column_index-1][0]):
            print('array[row_index][column_index-1]' + str(array[row_index][column_index-1]))
        if (array[row_index][column_index][0] ==  array[row_index+1][column_index-1][0]):
            print('array[row_index][column_index+1]' + str(array[row_index+1][column_index-1]))
    if (array[row_index][column_index][0] ==  array[row_index+1][column_index][0]):
            print('array[row_index+1][column_index]' + str(array[row_index+1][column_index]))
    if (array[row_index][column_index][0] ==  array[row_index+1][column_index+1][0]):
            print('array[row_index+1][column_index+1]' + str(array[row_index+1][column_index+1]))
            addCell(row_index+1,column_index+1)
    if (array[row_index][column_index][0] ==  array[row_index][column_index+1][0]):
            print('array[row_index][column_index+1]' + str(array[row_index][column_index+1]))
    #print ('index --- '+str(index))
    print ("pixel == "+ str(array[row_index-1][column_index]))
    
        #step = step+1
        #validateNeighbors(array, row_index, column_index, step, excluded_list)

    #return excluded_list

def addCell(c,r):
    color_continue=True
    excluded_list.append([c,r])

row_restriction = 3
column_restriction = 5
for row_index, line in enumerate(array):
    #print (line)
    for column_index, pixel in enumerate(line):
        '''if ((excluded[0] == column_index & excluded[1] == column_index) for excluded in excluded_list):
            print('Excluded,,, row_index =  '+str(row_index)+' column_index '+str(column_index))
        #if (excluded[0] == pixel[0] for excluded in excluded_list):
                '''
        if not color_continue:
            result[array[row_index][column_index][0]] = result[array[row_index][column_index][0]]+1
        validateNeighbors(array, row_index, column_index, 0, excluded_list)    
        break
    break
print ('excluded_list --- ' + str(excluded_list))
print ('result  '+str(result))
with open("output.txt", "w") as txt_file:
    for line in array:
        #print (line)
        txt_file.write(" ".join(str(line)) + "\n")



invimg = Image.fromarray(array)
invimg.save('shades-of-grey.png')


