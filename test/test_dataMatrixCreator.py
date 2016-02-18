import sys
import os
import filecmp

from __builtin__ import xrange

sys.path.append(os.path.dirname(os.getcwd())+"/src/")

from unittest import TestCase
import unittest
from data_matrix_creator import DataMatrixCreator

class TestDataMatrixCreator(TestCase):
    def test_create_data_matrix(self):
        DataMatrixCreator.create_data_matrix(600,666,6,"TestMatrix/")
        self.assertTrue(os.path.isfile("TestMatrix/666.jpg"))
        self.assertTrue(filecmp.cmp("TestMatrix/666.jpg","TestMatrix/666_template.jpg"))
    def test_create_blank(self):
        color = (205, 205, 205)
        im = DataMatrixCreator.create_blank(600,600,color)
        self.assertTrue(len(im) == 600)
        self.assertTrue(len(im[0]) == 600)
        for x in xrange(im.shape[0]):
            for y in xrange(im.shape[1]):
                self.assertTrue(im[x][y][0]==color[0])

    def test_remove_data_matrix(self):
        DataMatrixCreator.create_data_matrix(600,888,6,"TestMatrix/")
        DataMatrixCreator.remove_data_matrix(888,"TestMatrix/")
        self.assertFalse(os.path.isfile("TestMatrix/888.jpg"))

if __name__ == "__main__":
    unittest.main()
