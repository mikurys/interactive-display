import sys
import os
sys.path.append(os.path.dirname(os.getcwd())+"/src/")

from unittest import TestCase
from data_matrix_creator import DataMatrixCreator

class TestDataMatrixCreator(TestCase):
    def test_create_data_matrix(self):
        DataMatrixCreator.create_data_matrix(600,666,6,"TestMatrix/")
        self.assertTrue(os.path.isfile("TestMatrix/666.jpg"))

    def test_create_blank(self):
        color = (205, 205, 205)
        im = DataMatrixCreator.create_blank(600,600,color)
        for x in len(im):
            for y in len(im[0]):
                self.assertTrue(im[x][y] == color)

    def test_remove_data_matrix(self):
        DataMatrixCreator.create_data_matrix(600,666,6,"TestMatrix/")
        DataMatrixCreator.remove_data_matrix(666,"TestMatrix/")
        self.assertFalse(os.path.isfile("TestMatrix/666.jpg"))
