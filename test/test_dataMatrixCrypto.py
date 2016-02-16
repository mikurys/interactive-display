from unittest import TestCase
from data_matrix_crypto import DataMatrixCrypto
# temp tests:
# print(DataMatrix.encode(2678));
# print(DataMatrix.decode()); #683

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
        arr = [[1,0,1,0,1,0],[1,0,0,0,0,1],[1,0,0,1,0,0],[1,1,0,1,0,1],[1,1,0,1,1,0],[1,1,1,1,1,1]]
        expect = 683
        self.assertTrue(DataMatrixCrypto.decode(arr) == expect)
