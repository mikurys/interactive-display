import numpy as np
import cv2
from data_matrix_crypto import DataMatrixCrypto
import os

"""data_matrix_creator.py:

__author__ = "Ryszard Mikulec" """


class DataMatrixCreator:
    @staticmethod
    def create_data_matrix(image_size, mat_id, matrix_size, path='data_matrixes/'):
	""" param image_size
            param id of matrix to draw
            param matrix_size - size square matrix
            param path to save the image

        Function draw data matrix and save it.
        """
        matrix = DataMatrixCrypto.encode(mat_id)
        square_size = image_size // matrix_size
        image = DataMatrixCreator.create_blank(image_size, image_size)
        cv2.rectangle(image, (0, 0), (image_size - 1, image_size - 1), (0, 0, 0), 1, 1)
        for i in range(matrix_size):
            for j in range(matrix_size):
                if matrix[-i-1][j] == 1:
                    pt1 = (i * square_size, j * square_size)
                    pt2 = ((i+1) * square_size, (j+1) * square_size)
                    cv2.rectangle(image, pt1, pt2, (0, 0, 0), cv2.FILLED, 1)
        cv2.imwrite(path + str(mat_id) + '.jpg', image)

    @staticmethod
    def create_blank(width, height, rgb_color=(255, 255, 255)):
	""" param width of image
            param height of image
            param rgb_color - color of image defoult white
            Return blank image

        Function create blank image.
        """
        image = np.zeros((height, width, 3), np.uint8)
        color = tuple(reversed(rgb_color))
        image[:] = color
        return image

    @staticmethod
    def remove_data_matrix(mat_id, path='data_matrixes/'):
	"""param id of matrix
           param path to the directory with data matrixes

        Function remove data matrix from directory.
        """
        os.remove(path + str(mat_id) + '.jpg')

if __name__ == "__main__":
    DataMatrixCreator.create_data_matrix(600, 8289, 6)
