import sys
import os
sys.path.append(os.path.dirname(os.getcwd())+"/src/")
from unittest import TestCase
from db_connection import DBConnection


class TestDBConnection(TestCase):

    def test_insert_object(self):
        db = DBConnection("../data_base/test_base.db")
        db.clear()
        self.assertRaises(DBConnection("RANDOM_BASE"))
        self.assertTrue(db.get_object_count() == 0)
        db.insert_object(1, "1")
        self.assertTrue(db.get_object_count() == 1)
        self.assertTrue(db.get_object_name(1) == "1")
        db.clear()
        self.assertTrue(db.get_object_count() == 0)

    def test_insert_slide(self):
        db = DBConnection("../data_base/test_base.db")
        self.assertTrue(db.get_slide_count() == 0)
        db.insert_slide(1, "1")
        self.assertTrue(db.get_slide_count() == 1)
        self.assertTrue(db.get_slide_name(1) == "1")
        db.clear()
        self.assertTrue(db.get_slide_count() == 0)

    def test_get_object_list(self):
        db = DBConnection("../data_base/test_base.db")
        self.assertTrue(db.get_object_count() == 0)
        db.insert_object(1, "1")
        db.insert_object(2, "2")
        db.insert_object(3, "3")
        db.insert_object(4, "4")
        db.insert_object(5, "5")
        db.insert_object(6, "6")
        self.assertTrue(db.get_object_count() == 6)
        test_list = db.get_object_list()
        self.assertTrue(test_list[0][1] == "1")
        self.assertTrue(test_list[1][1] == "2")
        self.assertTrue(test_list[2][1] == "3")
        self.assertTrue(test_list[3][1] == "4")
        self.assertTrue(test_list[4][1] == "5")
        self.assertTrue(test_list[5][1] == "6")
        db.clear()
        self.assertTrue(db.get_object_count() == 0)

    def test_delete_object(self):
        db = DBConnection("../data_base/test_base.db")
        self.assertTrue(db.get_object_count() == 0)
        db.insert_object(1, "1")
        self.assertTrue(db.get_object_count() == 1)
        self.assertTrue(db.get_object_name(1) == "1")
        db.delete_object(1)
        self.assertTrue(db.get_object_count() == 0)
        db.clear()

    def test_get_slide_list(self):
        db = DBConnection("../data_base/test_base.db")
        self.assertTrue(db.get_slide_count() == 0)
        db.insert_slide(1, "1")
        db.insert_slide(2, "2")
        db.insert_slide(3, "3")
        db.insert_slide(4, "4")
        db.insert_slide(5, "5")
        db.insert_slide(6, "6")
        self.assertTrue(db.get_slide_count() == 6)
        test_list = db.get_slide_list()
        self.assertTrue(test_list[0][2] == "1")
        self.assertTrue(test_list[1][2] == "2")
        self.assertTrue(test_list[2][2] == "3")
        self.assertTrue(test_list[3][2] == "4")
        self.assertTrue(test_list[4][2] == "5")
        self.assertTrue(test_list[5][2] == "6")
        db.clear()
        self.assertTrue(db.get_object_count() == 0)

    def test_delete_slide(self):
        db = DBConnection("../data_base/test_base.db")
        self.assertTrue(db.get_slide_count() == 0)
        db.insert_slide(1, "1")
        self.assertTrue(db.get_slide_count() == 1)
        self.assertTrue(db.get_slide_name(1) == "1")
        db.delete_slide(1)
        self.assertTrue(db.get_slide_count() == 0)
