import numpy as np
import cv2
import sys


class DataMatrixDetector:
    def __init__(self, video):
        self.video = cv2.VideoCapture(video)
        self.is_detected = False

    def take_frame(self):
        ret, self.frame = video.read()
        return ret

    def detect_matrix(self):
        pass

    def setup_roi(self, row, height, column, width):
        self.tracked_matrix=(column, row, width, height)
        roi = frame[row:row+height, column:column+width]
        hsv_roi =  cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
        self.roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])
        cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)
        self.term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )

    def track_matrix(self):
        while(True):
            if take_frame():
                hsv = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)
                dst = cv2.calcBackProject([hsv],[0],self.roi_hist,[0,180],1)
                # apply meanshift to get the new location
                ret, track_window = cv2.CamShift(dst, self.tracked_matrix, self.term_crit)
                #pts = cv2.boxPoints(ret)
                #pts = np.int0(pts)
                #img2 = cv2.polylines(frame,[pts],True, 255,2)
            else:
                break
