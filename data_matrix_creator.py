import numpy as np
import cv2
from data_matrix_crypto import DataMatrixCrypto
import os

"""data_matrix_creator.py:

__author__ = "Ryszard Mikulec" """


class DataMatrixCreator:
    @staticmethod
    def create_data_matrix(image_size, id, matrix_size, path='data_matrixes/'):
        matrix = DataMatrixCrypto.encode(id)
        square_size = image_size // matrix_size
        image = DataMatrixCreator.create_blank(image_size, image_size)
        cv2.rectangle(image, (0, 0), (image_size - 1, image_size - 1), (0, 0, 0), 1, 1)
        for i in range(matrix_size):
            for j in range(matrix_size):
                if matrix[-i-1][j] == 1:
                    pt1 = (i * square_size, j * square_size)
                    pt2 = ((i+1) * square_size, (j+1) * square_size)
                    cv2.rectangle(image, pt1, pt2, (0, 0, 0), cv2.FILLED, 1)
        cv2.imwrite(path + str(id) + '.jpg', image)

    @staticmethod
    def create_blank(width, height, rgb_color=(255, 255, 255)):
        image = np.zeros((height, width, 3), np.uint8)
        color = tuple(reversed(rgb_color))
        image[:] = color
        return image

    def remove_data_matrix(id, path='data_matrixes/'):
        os.remove(path + str(id) + '.jpg')

if __name__ == "__main__":
    DataMatrixCreator.create_data_matrix(600, 8289, 6)
