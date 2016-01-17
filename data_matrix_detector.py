import numpy as np
import cv2
from data_matrix_crypto import DataMatrixCrypto

"""data_matrix_detector.py: Can detext and read data matrix but not always.It would be good to improwe detect_matrix method.

__author__ = "Ryszard Mikulec" """


class DataMatrixDetector:
    def __init__(self, video, size=6):
        self.video = cv2.VideoCapture(video)
        self.window = cv2.namedWindow("okno", cv2.WINDOW_NORMAL)
        self.size = size
        self.frame = None
        self.contours = None
        self.th = None

    def set_template(self, template):
        img = cv2.imread(template, 0)
        blur = cv2.GaussianBlur(img, (5, 5), 0)
        ret, thtemplate = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        im, template_contours, hierarchy2 = cv2.findContours(thtemplate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        self.contours = [contour for contour in template_contours if 5000 < cv2.contourArea(contour) < 100000]
        print(len(self.contours))

    def take_frame(self):
        ret, self.frame = self.video.read()
        return ret

    def check_matrix(self, matrix):
        for i in range(self.size):
            if (matrix[0][i] + matrix[-1][i] == i % 2 or matrix[0][i] + matrix[-1][i] == (i + 1) % 2) and (
                                matrix[i][0] + matrix[i][-1] == i % 2 or matrix[i][0] + matrix[i][-1] == (i + 1) % 2):
                pass
            else:
                return False
        for i in range(self.size):
            for j in range(self.size):
                if matrix[i][j] > 1:
                    return False
        return True

    def turn_matrix(self, matrix):
        if matrix[0][0] == 1:
            tab = [[(matrix[-j - 1][i] + 1) % 2 for j in range(self.size)] for i in range(self.size)]
        elif matrix[0][1] == 1:
            tab = [[(matrix[i][j] + 1) % 2 for j in range(self.size)] for i in range(self.size)]
        elif matrix[1][0] == 1:
            tab = [[(matrix[i][j] + 1) % 2 for j in range(self.size)] for i in range(self.size)]
        else:
            tab = [[(matrix[j][-1 - i] + 1) % 2 for j in range(self.size)] for i in range(self.size)]
        print(tab)
        return tab

    def read_matrix(self, rect):
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
            print(DataMatrixCrypto.decode(self.turn_matrix(matrix)))
        else:
            print(False)

    def take_contours(self):
        gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        ret, self.th = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        im2, contours, hierarchy = cv2.findContours(self.th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        return [contour for contour in contours if 3000 < cv2.contourArea(contour) < 130000]

    def detect_matrix(self):
        contours = self.take_contours()
        counter = 0
        for cnt, cnt2 in zip(contours, self.contours):
            val = cv2.matchShapes(cnt, cnt2, 1, 0.0)
            if val < 0.2:
                rect = cv2.minAreaRect(cnt)
                box = cv2.boxPoints(rect)
                box = np.int0(box)
                cv2.drawContours(self.frame, [box], 0, (0, 0, 255), 2)
                cv2.drawContours(self.frame, cnt, -1, (255, 0, 0), 3)
                counter += 1
        if counter == 1:
            self.read_matrix(box)

    def run(self):
        while True:
            if self.take_frame():
                self.detect_matrix()
                cv2.imshow("okno", self.frame)
                cv2.waitKey(40)
            else:
                break


if __name__ == "__main__":
    detector = DataMatrixDetector(0)
    detector.set_template("../template.jpg")
    detector.run()
