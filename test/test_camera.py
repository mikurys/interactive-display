import sys

from __builtin__ import xrange

sys.path.append("../src/")
import cv2
from unittest import TestCase
import unittest

from camera_handler import Camera
class Events:
    def __init__(self):
        self.onError=False
        self.onStart=False
        self.onClose=False
        self.onCapture=False

    def Error(self):
        self.onError = True
    def Start(self):
        self.onStart = True
    def Close(self):
        self.onClose = True
    def Capture(self):
        self.onCapture = True

class TestCamera(TestCase):
    def test_take_frame(self):
        cam = Camera()
        cam.video = cv2.VideoCapture(0)
        cam.window = cv2.namedWindow("Test", cv2.WINDOW_NORMAL)
        self.assertTrue(cam.take_frame)

    def test_run(self):
        cam = Camera()
        ev = Events()
        cam.OnError += ev.Error
        cam.OnStart += ev.Start
        cam.OnClose += ev.Close
        cam.OnCapture += ev.Capture
        cam.run()
        self.assertTrue(ev.onStart)
        self.assertFalse(ev.onError)

    def test_get_count(self):
        self.assertGreater(Camera.get_count(),0)

if __name__ == "__main__":
    unittest.main()