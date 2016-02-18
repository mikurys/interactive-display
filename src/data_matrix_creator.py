import os
import logging
import numpy as np
import cv2
from data_matrix_crypto import DataMatrixCrypto

"""data_matrix_creator.py:

__author__ = "Ryszard Mikulec" """


class DataMatrixCreator:
    @staticmethod
    def create_data_matrix(image_size, mat_id, matrix_size, path='data_matrixes/'):
        """
            @param image_size
            @param mat_id id of matrix to draw
            @param matrix_size - size square matrix
            @param path to save the image
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
                    cv2.rectangle(image, pt1, pt2, (0, 0, 0), -1, 1)
        cv2.imwrite(path + str(mat_id) + '.jpg', image)

    @staticmethod
    def create_blank(width, height, rgb_color=(255, 255, 255)):
        """
            @param width of image
            @param height of image
            @param rgb_color - color of image default white
            Return blank image
            Function creates blank image.
        """
        image = np.zeros((height, width, 3), np.uint8)
        color = tuple(reversed(rgb_color))
        image[:] = color
        return image

    @staticmethod
    def remove_data_matrix(mat_id, path='data_matrixes/'):
        """
            @param mat_id of matrix
            @param path to the directory with data matrixes
            Function removes data matrix from directory.
        """
        os.remove(path + str(mat_id) + '.jpg')
        logging.debug("Data Matrix - " + str(mat_id) + " removed")
