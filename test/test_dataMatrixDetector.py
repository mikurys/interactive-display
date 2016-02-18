import sys

from __builtin__ import xrange

sys.path.append("../src/")
import cv2
from unittest import TestCase
import unittest
from data_matrix_detector import DataMatrixDetector

class TestDataMatrixDetector(TestCase):
    def test_set_template(self):
        db = DBConnection("../data_base/test_base.db")
        det = DataMatrixDetector(db)
        det.set_template("../data_matrixes/template.jpg")

        pass

    def test_check_matrix(self):
        self.fail()

    def test_turn_matrix(self):
        self.fail()

    def test_read_matrix(self):
        self.fail()

    def test_take_contours(self):
        self.fail()

    def test_detect_matrix(self):
        #you should take a picture and name it test.jpg"
        pass
        capture = cv2.imread("test.jpg")
        db = DBConnection("../data_base/test_base.db")
        det = DataMatrixDetector(db)
        det.set_template("../data_matrixes/template.jpg")
        capture = det.detect_matrix([capture])

if __name__ == "__main__":
    unittest.main()