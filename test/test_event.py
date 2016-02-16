from unittest import TestCase
from camera_handler import Event


def method():
    return 1

def method2():
    return 2

class TestEvent(TestCase):
    def test_add(self):
        test = Event()
        test += method
        test += method2
        test += method2
        self.assertTrue(test.get_count() == 2)

    def test_remove(self):
        test = Event()
        self.assertTrue(test.get_count() == 0)
        test += method2
        test += method
        self.assertTrue(test.get_count() == 2)
        test -= method
        self.assertTrue(test.get_count() == 1)



