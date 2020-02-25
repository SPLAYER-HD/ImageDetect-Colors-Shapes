"""from skimage import io
import skimage
import os
filename = os.path.join(skimage.data_dir, '/home/splayer/Downloads/shades-of-grey2.png')
camera = io.imread(filename)
"""
import numpy as np
from PIL import Image
import sys
import faulthandler; faulthandler.enable()
import resource
import platform
import sys


class Classsify():
    def memory_limit(self):
        soft, hard = resource.getrlimit(resource.RLIMIT_AS)
        
        resource.setrlimit(resource.RLIMIT_AS, (self.get_memory(), hard))

    def get_memory(self):
        with open('/proc/meminfo', 'r') as mem:
            free_memory = 0
            for i in mem:
                sline = i.split()
                if str(sline[0]) in ('MemFree:', 'Buffers:', 'Cached:'):
                    free_memory += int(sline[1])
        print (free_memory)
        return free_memory
   
    def run(self):
        #self.memory_limit() 
        img = Image.open('shades-of-grey.png')
        img.thumbnail((256,256))

        self.array = np.array(img)
        self.array.setflags(write=True)

        #self.array[0][0] = [0,0,0]
        '''
        self.array[0][1] = [0,255,255]
        self.array[1][0] = [0,255,255]

        self.array[3][0] = [0,0,0]
        self.array[3][1] = [0,0,0]
        self.array[3][2] = [0,0,0]
        self.array[3][3] = [0,0,0]
        self.array[0][3] = [0,0,0]
        self.array[1][3] = [0,0,0]
        self.array[2][3] = [0,0,0]
        #self.array[3][3] = [0,0,0]
        #self.array[1][1] = [0,0,0]
        #self.array[1][1] = [0,0,0]
        #self.array[0][255] = [0,0,0]
        #print(str(self.array[0][0]))
        '''
        #euclidean distance 
        '''dist = (self.array[0] - self.array[1])**2
        dist = np.sum(dist, axis=1)
        dist = np.sqrt(dist)
        print (dist)
        '''
        self.color_continue=False
        self.result = [0] *256
        self.excluded_list = []
        '''print ('self.array[0[0]  '+str(self.array[0][0]))
        print ('excluded_list[0]  '+str(excluded_list[0]))
        '''
        sys.setrecursionlimit(200000)
        row_restriction = 2
        column_restriction = 2
        for row_index, line in enumerate(self.array):
            #print (line)
            for column_index, pixel in enumerate(line):
                '''if ((excluded[0] == column_index & excluded[1] == column_index) for excluded in excluded_list):
                    print('Excluded,,, row_index =  '+str(row_index)+' column_index '+str(column_index))
                #if (excluded[0] == pixel[0] for excluded in excluded_list):
                        '''
                #print ('for column   --  color_continue  == '+str(self.color_continue))
                #if not self.color_continue:
                vertex_list = self.get_vertex(row_index, column_index)
                #if not (excluded[0] == row_index & excluded[1] == column_index for excluded in self.excluded_list):
                    #print ('enerrrrS')
                if  not self.isAlreadyChecked(row_index,column_index):
                    print ('. ')
                    #print ('point to evaluate -- > r ='+str(row_index)+', c='+str(column_index))
                    self.result[self.get_value(row_index, column_index)] = self.result[self.get_value(row_index, column_index)]+1
                    print ('result  '+str(self.result))
                    #if (excluded[0] == pixel[0] for excluded in excluded_list):
                    self.validateNeighbors(row_index, column_index, vertex_list)
                #if column_index >column_restriction:
                    #break
            #if row_index >row_restriction:
                #print('row_index foinished '+str(row_index))
                #break
        print ('result  '+str(self.result))
        with open("output.txt", "w") as txt_file:
            for line in self.array:
                #print (line)
                txt_file.write(" ".join(str(line)) + "\n")

        invimg = Image.fromarray(self.array)
        invimg.save('shades-of-grey.png')
    def get_value(self, r, c):
        return self.array[r][c]
        #return self.array[r][c][0]

    def get_vertex(self, row_index, column_index):
        vertex = []
        #print ('get vertex '+str(row_index)+'  '+str(column_index))
        if self.isPositive(row_index):
            if not self.isAlreadyChecked(row_index-1, column_index):
                vertex.append([row_index-1,column_index])
        if self.isPositive(column_index):
            if not self.isAlreadyChecked(row_index, column_index-1):
                vertex.append([row_index,column_index-1])
        if row_index+1 < len(self.array):
            if not self.isAlreadyChecked(row_index+1, column_index):
                vertex.append([row_index+1,column_index])
        if column_index+1 < len(self.array[0]):
            if not self.isAlreadyChecked(row_index, column_index+1):
                vertex.append([row_index,column_index+1])
        #print('vertes responde '+str(vertex))
        return vertex


    def isAlreadyChecked(self, row_index, column_index):
        #print ('isAlreadyChecked -- > self.excluded_list == '+str(self.excluded_list))
        #print ('isAlreadyChecked -- > row_index == '+str(row_index)+ ', column_index == '+str(column_index))
        #if any(excluded[0] == row_index & excluded[1] == column_index for excluded in self.excluded_list):
        for excluded in self.excluded_list:
            #print ("exclude single "+str(excluded))
            #print ("exclude single 0 ="+str(excluded[0]))
            #print ("exclude single 1 ="+str(excluded[1]))
            if excluded[0] == row_index and excluded[1] == column_index:
                #print ('isAlreadyChecked -- > return true == ')
                return True
        #print ('isAlreadyChecked -- > return False == ')
        return False


    def isPositive(self, value):
        return value-1 >=0
    
    
    def validateNeighbors(self, row_index, column_index, vertex_list):
        #print ('Start Validate Neighbor')
        #print ('row_index == '+str(vertex_list))

        #print ('pixel  --- '+str(self.array[row_index][column_index][0]))
        self.color_continue=False
        #while (step <8):
        
        #print('step '+str(step))
        near_cell = None
        new_vertex_list = []
        for vertex in vertex_list:

            if (self.get_value(row_index, column_index) ==  self.get_value(vertex[0], vertex[1])):
                #print('self.array[row_index-1][column_index]' + str(self.array[row_index-1][column_index]))
                #print ("pixel == "+ str(self.get_value(vertex[0], vertex[1])))
                self.addCell(vertex[0],vertex[1])
                #print ('vertex[0] ' +str(vertex[0]))
                #print ('vertex[1] ' +str(vertex[1]))
                
                self.validateNeighbors(vertex[0],vertex[1], self.get_vertex(vertex[0],vertex[1]))
            #print ('index --- '+str(index))
        #print ('color_continue  == '+str(self.color_continue))
                #step = step+1
            #if(self.color_continue):
                #validateNeighbors(self.array, row_index, column_index, step, excluded_list)

        #return excluded_list

    def addCell(self, r,c):
        #print('addCell  r c  '+ str(r)+' '+str(c))
        self.color_continue=True
        self.excluded_list.append([r,c])
        #self.array[c][r] = [0,0,0]
    
if __name__ == "__main__":
    print('Executed as main program')
    classsify = Classsify()
    classsify.run()
    