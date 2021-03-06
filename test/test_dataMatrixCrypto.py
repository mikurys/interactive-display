import sys
import os

sys.path.append(os.path.dirname(os.getcwd())+"/src/")
from unittest import TestCase
from data_matrix_crypto import DataMatrixCrypto


class TestDataMatrixCrypto(TestCase):
    def test_encode(self):
        expect = [[1, 0, 1, 0, 1, 0],
                  [1, 0, 0, 0, 0, 1],
                  [1, 1, 0, 1, 0, 0],
                  [1, 0, 1, 1, 1, 1],
                  [1, 0, 1, 1, 0, 0],
                  [1, 1, 1, 1, 1, 1]]
        arr = DataMatrixCrypto.encode(2678)
        self.assertTrue(arr == expect)


    def test_decode(self):
        arr = [[1, 0, 1, 0, 1, 0],
               [1, 0, 0, 0, 0, 1],
               [1, 0, 0, 1, 0, 0],
               [1, 1, 0, 1, 0, 1],
               [1, 1, 0, 1, 1, 0],
               [1, 1, 1, 1, 1, 1]]
        expect = 683
        self.assertTrue(DataMatrixCrypto.decode(arr) == expect)
        before = 62792
        matrix = DataMatrixCrypto.encode(before)
        after = DataMatrixCrypto.decode(matrix)
        self.assertTrue(before == after)


