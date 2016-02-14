import sqlite3


class DBConcetion:
    def __init__(self, data_base):
        self.connection = sqlite3.connect(data_base)

    def insert_object(self, id, name):
        self.connection.execute("INSERT INTO object (id, name) VALUES (" + id + ", '" + name + "')")
        self.connection.commit()

    def insert_slide(self, object_id, file_name):
        self.connection.execute("INSERT INTO slide (object_id, file_name) VALUES (" +
                                str(object_id) + ", '" + file_name + "')")
        self.connection.commit()

    def get_object_list(self):
        return self.connection.execute("SELECT id, name FROM object")

    def delete_object(self, id):
        self.connection.execute("Delete FROM object WHERE id=" + id + ";")
        self.connection.commit()

    def get_slide_list(self):
        return self.connection.execute("SELECT id, object_id, file_name FROM slide ORDER BY id")

    def delete_slide(self, file_name):
        self.connection.execute("Delete FROM slide WHERE file_name='" + file_name + "';")
        self.connection.commit()
