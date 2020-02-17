"""Class to classify shapes on images own algorithm - Diego (only works with tiny images)"""

import os
import numpy as np
from PIL import Image
import sys


class Classsify():
    ''' class to classify'''
    def run(self, result):
        print ('Running my own algorithm')
        image_path = '/resources/'+os.getenv('SMALL_IMAGE', 'small-shades-of-grey.png')
        img = Image.open(image_path)
        img.thumbnail((256,256))    

        self.array = np.array(img)
        self.array.setflags(write=True)

        self.color_continue=False
        self.result = [0] *256
        self.excluded_list = []

        sys.setrecursionlimit(200000)
        for row_index, line in enumerate(self.array):
            for column_index, pixel in enumerate(line):
                vertex_list = self.get_vertex(row_index, column_index)
                if  not self.isAlreadyChecked(row_index,column_index):
                    self.result[self.get_value(row_index, column_index)] = self.result[self.get_value(row_index, column_index)]+1
                    self.validateNeighbors(row_index, column_index, vertex_list)

        return self.result

    def get_value(self, r, c):
        return self.array[r][c]
        #return self.array[r][c][0]

    def get_vertex(self, row_index, column_index):
        vertex = []
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
        return vertex

    def isAlreadyChecked(self, row_index, column_index):
        for excluded in self.excluded_list:
            if excluded[0] == row_index and excluded[1] == column_index:
                return True
        return False

    def isPositive(self, value):
        return value-1 >=0

    def validateNeighbors(self, row_index, column_index, vertex_list):
        self.color_continue=False
        for vertex in vertex_list:
            if (self.get_value(row_index, column_index) ==  self.get_value(vertex[0], vertex[1])):
                self.addCell(vertex[0],vertex[1])
                self.validateNeighbors(vertex[0],vertex[1], self.get_vertex(vertex[0],vertex[1]))

    def addCell(self, r,c):
        self.color_continue=True
        self.excluded_list.append([r,c])
