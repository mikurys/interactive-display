import sys

from __builtin__ import xrange

sys.path.append("../src/")
import cv2
from unittest import TestCase
import unittest
from data_matrix_detector import DataMatrixDetector
from db_connection import DBConnection

class TestDataMatrixDetector(TestCase):
    def test_set_template(self):
        db = DBConnection("../data_base/test_base.db")
        det = DataMatrixDetector(db)
        det.set_template("../data_matrixes/template.jpg")
        self.assertGreater(len(det.contours),0)

    def test_check_matrix(self):
        expect = [[1, 0, 1, 0, 1, 0],
                  [1, 0, 0, 0, 0, 1],
                  [1, 1, 0, 1, 0, 0],
                  [1, 0, 1, 1, 1, 1],
                  [1, 0, 1, 1, 0, 0],
                  [1, 1, 1, 1, 1, 1]]
        #rotated to the right
        test = [[1,1,1,1,1,1],
                [0,0,1,0,0,1],
                [1,0,0,1,1,1],
                [0,0,1,1,1,1],
                [1,0,0,1,0,1],
                [0,1,0,1,0,1]]

        db = DBConnection("../data_base/test_base.db")
        det = DataMatrixDetector(db)
        det.set_template("../data_matrixes/template.jpg")
        self.assertTrue(det.check_matrix(expect))
        self.assertFalse(det.check_matrix(test))

    def test_turn_matrix(self):

        expect = [[1, 0, 1, 0, 1, 0],
                  [1, 0, 0, 0, 0, 1],
                  [1, 1, 0, 1, 0, 0],
                  [1, 0, 1, 1, 1, 1],
                  [1, 0, 1, 1, 0, 0],
                  [1, 1, 1, 1, 1, 1]]
        #rotated to the right
        test = [[1,1,1,1,1,1],
                [0,0,1,0,0,1],
                [1,0,0,1,1,1],
                [0,0,1,1,1,1],
                [1,0,0,1,0,1],
                [0,1,0,1,0,1]]

        db = DBConnection("../data_base/test_base.db")
        det = DataMatrixDetector(db)
        det.set_template("../data_matrixes/template.jpg")
        test = det.turn_matrix(test)
        self.assertEqual(test,expect)


    def test_detect_matrix(self):
        #you should take a picture of a matrix and name it test.jpg"

     #   capture = cv2.imread("TestImages/test.jpg")
     #   db = DBConnection("../data_base/test_base.db")
     #   det = DataMatrixDetector(db)
     #   det.set_template("../data_matrixes/template.jpg")
     #   capture = det.detect_matrix([capture])
     #   self.assertTrue(det.detected)
        pass

if __name__ == "__main__":
    unittest.main()