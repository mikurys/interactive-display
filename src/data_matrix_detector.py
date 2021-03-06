import logging
import numpy as np
import cv2
from data_matrix_crypto import DataMatrixCrypto
from info_displayer import InfoDisplayer

"""data_matrix_detector.py: Can detext and read data matrix but not always.
It would be good to improve detect_matrix method.

__author__ = "Ryszard Mikulec" """


class DataMatrixDetector:
    def __init__(self, db, size=6):
        self.info_displayer = InfoDisplayer(db)
        self.size = size
        self.frame = None
        self.contours = None
        self.th = None
        self.detected = False
        self.id = None

    def set_template(self, template):
        """
            @param template string like 'path/filename' of template image
            Function set template that will be used to detect matrix.
        """
        img = cv2.imread(template, 0)
        blur = cv2.GaussianBlur(img, (5, 5), 0)
        ret, thtemplate = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        im, template_contours, hierarchy2 = cv2.findContours(thtemplate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        self.contours = [contour for contour in template_contours if 5000 < cv2.contourArea(contour) < 100000]
        logging.debug("Template "+template + " set. Contours length: "+ str(len(self.contours)) )

    def check_matrix(self, matrix):
        """
            @param matrix
            Return true if matrix is data matrix or false if not
            Function verify matrix are data matrix.
        """
        for i in range(self.size):
            if (matrix[0][i] + matrix[-1][i] == i % 2 or matrix[0][i] + matrix[-1][i] == (i + 1) % 2) and (
                                matrix[i][0] + matrix[i][-1] == i % 2 or matrix[i][0] + matrix[i][-1] == (i + 1) % 2):
                pass
            else:
                logging.debug("Matrix detection failed. Matrix passed to function " + str(matrix))
                return False
        for i in range(self.size):
            for j in range(self.size):
                if matrix[i][j] > 1:
                    logging.debug("Matrix detection failed. Matrix passed to function " + str(matrix))
                    return False
        logging.info("Matrix detected : " + str(matrix))
        return True

    def turn_matrix(self, matrix):
        """
            @param matrix
            @return well oriented matrix
            Function make matrix well oriented.
        """
        if matrix[0][0] == 1:
            tab = [[(matrix[-j - 1][i] + 1) % 2 for j in range(self.size)] for i in range(self.size)]
        elif matrix[0][1] == 1:
            tab = [[(matrix[i][j] + 1) % 2 for j in range(self.size)] for i in range(self.size)]
        elif matrix[1][0] == 1:
            tab = [[(matrix[i][j] + 1) % 2 for j in range(self.size)] for i in range(self.size)]
        else:
            tab = [[(matrix[j][-1 - i] + 1) % 2 for j in range(self.size)] for i in range(self.size)]
        return tab

    def read_matrix(self, rect):
        """
            @param rect is two dimention array with point of a rectangle surrounding matrix area on image
            @return true if matrix is read succesfully or false if not
            Function read matrix in selected area.
        """
        wx = (rect[1][0] - rect[0][0]) / self.size
        wy = (rect[1][1] - rect[0][1]) / self.size
        vx = (rect[3][0] - rect[0][0]) / self.size
        vy = (rect[3][1] - rect[0][1]) / self.size
        first = [rect[0][0] + (wx + vx) / 2, rect[0][1] + (wy + vy) / 2]
        try:
            matrix = [[self.th[first[1] + i * wy + j * vy][first[0] + i * wx + j * vx] for i in range(self.size)] for j
                      in range(self.size)]
        except IndexError:
            return None
        if self.check_matrix(matrix):
            print(True)
            self.detected = True
            print(matrix)
            self.id = DataMatrixCrypto.decode(self.turn_matrix(matrix))
            print(matrix)
            print(self.id)
            return True
        else:
            self.detected = False
            return False

    def take_contours(self):
        """
            @return contours of objects find on image
            Function find contours on image
        """
        gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        ret, self.th = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        im2, contours, hierarchy = cv2.findContours(self.th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        return [contour for contour in contours if 1000 < cv2.contourArea(contour) < 150000]

    def detect_matrix(self, current_frame):
        """
            @param current_frame is image where matrix is detecting
            Function detext matrix on image.
        """
        self.frame = current_frame[0]
        contours = self.take_contours()
        for cnt, cnt2 in zip(contours, self.contours):
            val = cv2.matchShapes(cnt, cnt2, 1, 0.0)
            if val < 0.2:
                rect = cv2.minAreaRect(cnt)
                box = cv2.boxPoints(rect)
                box = np.int0(box)
                if self.read_matrix(box):
                    cv2.drawContours(self.frame, [box], 0, (0, 0, 255), 2)
                    cv2.drawContours(self.frame, cnt, -1, (255, 0, 0), 3)
        if self.detected:
            img = self.info_displayer.display(self.id, self.frame)
            logging.debug("Data Matrix detected")
        current_frame = [self.frame]
