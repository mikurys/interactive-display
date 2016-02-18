import sys
sys.path.append("../src/")

from unittest import TestCase
from db_connection import DBConnection
from info_displayer import InfoDisplayer

class TestInfoDisplayer(TestCase):
    def test_display(self):
        db = DBConnection("data_base/test_base.db")
        disp = InfoDisplayer(db)

    def test_get_slide_name(self):
        self.fail()

    def test_get_first(self):
        self.fail()

    def test_get_next(self):
        self.fail()
