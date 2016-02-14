import cv2


class InfoDisplayer:
    def __init__(self, db, path='slides/'):
        self.path = path
        temp_list = db.get_object_list()
        self.object_list = [[x for x in row] + [''] for row in temp_list]
        temp_list = db.get_slide_list()
        self.slide_list = [row for row in temp_list]
        self.time = 0

    def display(self, id, img_dst):
        filename = self.get_slide_name(id)
        if filename == '':
            return img_dst
        try:
            img_src = cv2.imread(self.path + filename)
            x_offset = (img_dst.shape[1] - img_src.shape[1]) // 2
            y_offset = (img_dst.shape[0] - img_src.shape[0]) // 2
            img_dst[y_offset:y_offset+img_src.shape[0], x_offset:x_offset+img_src.shape[1]] = img_src
        except:
            print("Slide file not found")
        return img_dst

    def get_slide_name(self, id):
        slide = ''
        for object in self.object_list:
            if object[0] == id:
                if object[2] == '':
                    slide = object[2] = self.get_first(object)
                elif self.time < 5000:
                    slide = object[2]
                else:
                    slide = object[2] = self.get_next(object)
                    self.time = 0
        self.time += 40
        return slide

    def get_first(self, object):
        for slide in self.slide_list:
            if slide[1] == object[0]:
                return slide[2]
        return ''

    def get_next(self, object):
        is_current_find = False
        for slide in self.slide_list:
            if slide[2] == object[2]:
                is_current_find = True
                continue
            if is_current_find and slide[1] == object[0]:
                print("ERROR "*100)
                print(slide[2])
                return slide[2]
        return self.get_first(object)
