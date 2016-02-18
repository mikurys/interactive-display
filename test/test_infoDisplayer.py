import sys

from __builtin__ import xrange

sys.path.append("../src/")
import cv2
from unittest import TestCase
import unittest
from db_connection import DBConnection
from info_displayer import InfoDisplayer

class TestInfoDisplayer(TestCase):
    def test_display(self):
        db = DBConnection("../data_base/test_base.db")
        db.insert_slide("1","1.jpg")
        db.insert_object("1","LOL")
        disp = InfoDisplayer(db, "TestImages/")
        im = cv2.imread("TestImages/1.jpg")
        im2 = cv2.imread("TestImages/2.jpg")
        im2 = disp.display(1,im2)
        db.clear()
        self.assertTrue(len(im) == len(im2))
        for x in range(im.shape[0]):
            for y in range(im.shape[1]):
                self.assertTrue(im[x][y][0]==im2[x][y][0])

    def test_get_slide_name(self):
        db = DBConnection("../data_base/test_base.db")
        db.insert_slide("1","1.jpg")
        db.insert_object("1","LOL")
        disp = InfoDisplayer(db, "TestImages/")
        name = disp.get_slide_name(1)
        self.assertTrue(name == "1.jpg")
        db.clear()

    def test_get_first(self):
        db = DBConnection("../data_base/test_base.db")
        db.insert_slide("1","1.jpg")
        db.insert_slide("2","2.jpg")
        db.insert_object("1","LOL")
        db.insert_object("2","LOL")

        ob1 = (1,"LOL")
        ob2 = (2,"LOL")
        ob3 = (3,"LOL")
        disp = InfoDisplayer(db, "TestImages/")
        out = disp.get_first(ob1)
        self.assertTrue(out == "1.jpg")
        out = disp.get_first(ob2)
        self.assertTrue(out == "2.jpg")
        out = disp.get_first(ob3)
        self.assertTrue(out == "")
        db.clear()

    def test_get_next(self):
        db = DBConnection("../data_base/test_base.db")
        db.insert_slide("1","1.jpg")
        db.insert_slide("2","2.jpg")
        db.insert_slide("3","2.jpg")
        db.insert_slide("4","2.jpg")
        db.insert_object("1","LOL")
        db.insert_object("2","LOL")
        db.insert_object("3","LOL")
        db.insert_object("4","LOL")

        ob1 = (1,1,"LOL")
        ob2 = (2,2,"LOL")
        ob3 = (3,5,"LOL")
        disp = InfoDisplayer(db, "TestImages/")
        out = disp.get_next(ob1)
        self.assertTrue(out == "1.jpg")
        out = disp.get_next(ob2)
        self.assertTrue(out == "2.jpg")
        out = disp.get_next(ob3)
        self.assertTrue(out == "2.jpg")
        db.clear()

if __name__ == "__main__":
    unittest.main()
