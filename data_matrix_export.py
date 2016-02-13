import math
import numpy as np
import cv2
from data_matrix_crypto import DataMatrixCrypto


WHITE = [255,255,255]
BLACK = [0,0,0]

class DataMatrixExport:
    #exports matrix into image
    @staticmethod 
    def ExportMatrix(matrix,size,filename):

        img = np.zeros((size,size,3), np.uint8)
        rec_size = int( (size)/(len(matrix)+2) )
        #top line
        for i in range(0,size):
            for j in range(0,rec_size-1):
                if (math.floor(i/rec_size) % 2):
                    img[j,i] = WHITE
                else:
                    img[j,i] = BLACK
        #right line
        for i in range(0,size,1):
             for j in range(size-1,size-rec_size-1,-1):
                    if (math.floor(i/rec_size) % 2):
                        img[i,j] = BLACK
                    else:
                        img[i,j] = WHITE
        #data
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix)):
                if (matrix[i][j] == 0):
                    for x in range(0,rec_size):
                        for y in range(0,rec_size):
                            img[(i+1)*rec_size+x,(j+1)*rec_size +y] = WHITE
        #save
        cv2.imwrite(filename,img)

    #exports ready data matrix into image
    @staticmethod 
    def ExportDataMatrix(num,size,filename):
        
        matrix = DataMatrixCrypto.encode(num)
        rec_size = int(size/len(matrix))
        #black image
        img = np.zeros((size,size,3), np.uint8)
        #data
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix)):
                if (matrix[i][j] == 0):
                    for x in range(0,rec_size):
                        for y in range(0,rec_size):
                            img[i*rec_size+x,j*rec_size +y] = WHITE
        
        #save
        cv2.imwrite(filename,img)

