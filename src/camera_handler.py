# simple event-driven system for handling video cameras
import threading
import logging
import cv2


# basic event system
# usage inside the class
# self.myevent = Event() //create new event
# self.myevent += fun1() //assign first callback
# self.myevent += fun2() //assign second callback
# self.myevent -= fun2() //remove second callback
# print(len(self.myevent)) //number of callback functions assigned to event

class Event:
    def __init__(self):
        self.handlers = set()  # set is used so handler cannot be assinged more than one time

    def add(self, handler):
        self.handlers.add(handler)
        return self

    def remove(self, handler):
        try:
            self.handlers.remove(handler)
        except:
            raise ValueError("Callback is not assigned to event.")
        return self

    def trigger(self, *args, **kwargs):
        for handler in self.handlers:
            handler(*args, **kwargs)

    def get_count(self):
        return len(self.handlers)

    __iadd__ = add
    __isub__ = remove
    __call__ = trigger
    __len__ = get_count


class Camera(threading.Thread):
    def __init__(self, camera_number=0, window_name="window"):
        """
            Starts new thread and creates events
        """
        threading.Thread.__init__(self)
        self.video = None
        self.cam = camera_number
        self.window = None
        self.frame = None
        self.contours = None
        self.th = None
        self.visible = True
        self.window_name = window_name

        self.OnClose = Event()
        self.OnStart = Event()
        self.OnCapture = Event()
        self.OnUpdate = Event()
        self.OnError = Event()

    def take_frame(self):
        ret, self.frame = self.video.read()
        self.frame = [self.frame]
        return ret

    def run(self):
        """
            Starts main loop
        """
        try:
            self.video = cv2.VideoCapture(self.cam)
            self.window = cv2.namedWindow(self.window_name, cv2.WINDOW_NORMAL)
        except cv2.error as e:
            logging.error(logging.error("Error occured during setting up camera: " + e))
            self.OnError()
            return
        self.OnStart()
        while True:
            try:
                if self.take_frame():
                    self.OnCapture(self.frame)
                    if self.visible:
                        self.OnUpdate()
                        cv2.imshow(self.window_name, self.frame[0])
                    if cv2.waitKey(40) == 27:
                        self.OnClose()
                        logging.info("Main loop closed by user")
                        break
                else:
                    self.OnClose()
                    break
            except cv2.error as e:
                logging.error(logging.error("Error occured during camera operation: " + e))
                self.OnError()

    # get camera count

    @staticmethod
    def get_count():
        """
            Gets number of available cameras
        """
        n = 0
        for i in range(10):
            # noinspection PyBroadException
            try:
                cap = cv2.VideoCapture(i)
                ret, frame = cap.read()
                cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                cap.release()
                cv2.destroyAllWindows()
                n += 1
            except:
                cv2.destroyAllWindows()
                break
        return n
