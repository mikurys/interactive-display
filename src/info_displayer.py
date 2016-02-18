import logging
import cv2


class InfoDisplayer:

    def __init__(self, db, path='slides/'):
        self.path = path
        temp_list = db.get_object_list()
        self.object_list = [[x for x in row] + [''] for row in temp_list]
        temp_list = db.get_slide_list()
        self.slide_list = [row for row in temp_list]
        self.time = 0

    def display(self, slide_id, img_dst):
        filename = self.get_slide_name(slide_id)
        if not filename:
            return img_dst
        # noinspection PyBroadException
        try:
            img_src = cv2.imread(self.path + filename)
            x_offset = (img_dst.shape[1] - img_src.shape[1]) // 2
            y_offset = (img_dst.shape[0] - img_src.shape[0]) // 2
            img_dst[y_offset:y_offset+img_src.shape[0], x_offset:x_offset+img_src.shape[1]] = img_src
        except:
            logging.error("Slide file: " + filename + "not found")
        return img_dst

    def get_slide_name(self, slide_id):
        slide = ''
        for element in self.object_list:
            if element[0] == slide_id:
                if element[2] == '':
                    slide = element[2] = self.get_first(element)
                elif self.time < 5000:
                    slide = element[2]
                else:
                    slide = element[2] = self.get_next(element)
                    self.time = 0
        self.time += 40
        return slide

    def get_first(self, element):
        for slide in self.slide_list:
            if slide[1] == element[0]:
                return slide[2]
        return ''

    def get_next(self, element):
        is_current_find = False
        for slide in self.slide_list:
            if slide[2] == element[2]:
                is_current_find = True
                continue
            if is_current_find and slide[1] == element[0]:
                logging.error("Internal error: get_next found wrong element")
                return slide[2]
        return self.get_first(element)
