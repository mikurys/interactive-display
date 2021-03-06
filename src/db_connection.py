import sqlite3
import logging

class DBConnection:
    def __init__(self, data_base):
        try:
            self.connection = sqlite3.connect(data_base)
        except sqlite3.Error as e:
            logging.error("[" + self.__class__.__name__ + "] Error occured during init: " +e.args[0])

    def __del__(self):
        try:
            if hasattr(self, 'connection'):
                self.connection.close()
        except sqlite3.Error as e:
            logging.error("[" + self.__class__.__name__ + "] Error occured during closing: " +e.args[0])

    def insert_object(self, object_id, name):
        self.connection.execute("INSERT INTO object (id, name) VALUES (" + str(object_id) + ", '" + name + "')")
        self.connection.commit()

    def insert_slide(self, object_id, file_name):
        self.connection.execute("INSERT INTO slide (object_id, file_name) VALUES (" +
                                str(object_id) + ", '" + file_name + "')")
        self.connection.commit()

    def get_object_list(self):
        #return self.connection.execute("SELECT id, name FROM object")
        tmp = []
        for row in self.connection.execute("SELECT id, name FROM object"):
            tmp.append(row)
        return tmp

    def delete_object(self, id):
        self.connection.execute("Delete FROM object WHERE id=" + str(id) + ";")
        self.connection.commit()

    def get_slide_list(self):
        #return self.connection.execute("SELECT id, object_id, file_name FROM slide ORDER BY id")
        tmp = []
        for row in self.connection.execute("SELECT id, object_id, file_name FROM slide ORDER BY id"):
            tmp.append(row)
        return tmp

    def delete_slide(self, file_name):
        self.connection.execute("Delete FROM slide WHERE file_name='" + str(file_name) + "';")
        self.connection.commit()

    # Used for testing

    def clear(self):
        self.connection.execute("Delete FROM slide;")
        self.connection.execute("Delete FROM object;")
        self.connection.commit()
        logging.debug("[" + self.__class__.__name__ + "] Database cleared ")

    def get_object_count(self):
        return int(self.connection.execute("SELECT COUNT(*) FROM object;").fetchone()[0])

    def get_object_name(self,object_id):
        return self.connection.execute("SELECT name FROM object WHERE id=" + str(object_id) + ";").fetchone()[0]

    def get_slide_count(self):
        return int(self.connection.execute("SELECT COUNT(*) FROM slide;").fetchone()[0])

    def get_slide_name(self, object_id):
        return self.connection.execute("SELECT file_name FROM slide WHERE object_id =" + str(object_id) + ";").fetchone()[0]

    def execute_command(self, command):
        return self.connection.execute(command)

