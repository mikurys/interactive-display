import tkinter as tk
from data_matrix_detector import DataMatrixDetector
from db_connection import DBConcetion
from camera_handler import Camera
from data_matrix_creator import DataMatrixCreator


class InteractiveDisplay(tk.Frame):
    def __init__(self, master=None):
        self.db = DBConcetion("data_base/base.db")
        tk.Frame.__init__(self, master)
        self.pack()
        self.run_detector = tk.Button(self, text="Run detector", command=self.run)
        self.object_listbox = tk.Listbox(self)
        self.slide_listbox = tk.Listbox(self)
        self.object_id_label = tk.Label(self, text="Id:")
        self.object_name_label = tk.Label(self, text="Name:")
        self.object_id_entry = tk.Entry(self)
        self.object_name_entry = tk.Entry(self)
        self.file_name_label = tk.Label(self, text="File name:")
        self.object_name_label2 = tk.Label(self, text="Object name:")
        self.file_name_entry = tk.Entry(self)
        self.variable = tk.StringVar(self)
        self.object_name_optionmenu = tk.OptionMenu(self, self.variable, '')
        self.add_object_button = tk.Button(self, text="Add object", command=self.add_object)
        self.delete_object_button = tk.Button(self, text="Delete object", command=self.delete_object)
        self.delete_slide_button = tk.Button(self, text="Delete slide", command=self.delete_slide)
        self.add_slide_button = tk.Button(self, text="Add slide", command=self.add_slide)
        self.quit = tk.Button(self, text="Quit", fg="red", command=root.destroy)
        self.dict = None
        self.place_widgets()
        self.set_widgets()

    def set_widgets(self):
        self.set_optionmenu()
        self.set_object_listbox()
        self.set_slide_listbox()
        self.object_listbox.bind('<<ListboxSelect>>', self.onselect_object)
        self.slide_listbox.bind('<<ListboxSelect>>', self.onselect_slide)

    def place_widgets(self):
        self.run_detector.grid(row=0, columnspan=8)
        self.object_listbox.grid(row=1, column=0, columnspan=4)
        self.slide_listbox.grid(row=1, column=4, columnspan=4)
        self.object_id_label.grid(row=3, column=0)
        self.object_name_label.grid(row=3, column=2)
        self.object_id_entry.grid(row=3, column=1)
        self.object_name_entry.grid(row=3, column=3)
        self.file_name_label.grid(row=3, column=4)
        self.object_name_label2.grid(row=3, column=6)
        self.file_name_entry.grid(row=3, column=5)
        self.object_name_optionmenu.grid(row=3, column=7)
        self.add_object_button.grid(row=4, column=0, columnspan=2)
        self.delete_object_button.grid(row=4, column=2, columnspan=2)
        self.delete_slide_button.grid(row=4, column=6, columnspan=2)
        self.add_slide_button.grid(row=4, column=4, columnspan=2)
        self.quit.grid(row=5, columnspan=8)

    def onselect_object(self, evt):
        w = evt.widget
        index = int(w.curselection()[0])
        item = w.get(index)
        element = item.split(' - ')
        self.object_id_entry.delete(0, tk.END)
        self.object_id_entry.insert(0, element[0])
        self.object_name_entry.delete(0, tk.END)
        self.object_name_entry.insert(0, element[1])

    def onselect_slide(self, evt):
        w = evt.widget
        index = int(w.curselection()[0])
        item = w.get(index)
        slide = item.split(' - ')
        self.file_name_entry.delete(0, tk.END)
        self.file_name_entry.insert(0, slide[1])
        # self.variable.set(next((object for object, id in self.dict.items() if id == slide[0]), None))

    def add_object(self):
        self.db.insert_object(self.object_id_entry.get(), self.object_name_entry.get())
        DataMatrixCreator.create_data_matrix(600, self.object_id_entry.get(), 6)
        self.object_id_entry.delete(0, tk.END)
        self.object_name_entry.delete(0, tk.END)
        self.set_object_listbox()
        self.set_optionmenu()

    def delete_object(self):
        self.db.delete_object(self.object_id_entry.get())
        DataMatrixCreator.remove_data_matrix(self.object_id_entry.get())
        self.set_object_listbox()
        self.set_optionmenu()

    def add_slide(self):
        self.db.insert_slide(self.dict[self.variable.get()], self.file_name_entry.get())
        self.file_name_entry.delete(0, tk.END)
        self.set_slide_listbox()

    def delete_slide(self):
        self.db.delete_slide(self.file_name_entry.get())
        self.set_slide_listbox()

    def set_optionmenu(self):
        temp_list = self.db.get_object_list()
        self.dict = {row[1]: row[0] for row in temp_list}
        self.variable.set(list(self.dict.keys())[0])
        self.object_name_optionmenu = tk.OptionMenu(self, self.variable, *self.dict.keys())
        self.object_name_optionmenu.grid(row=3, column=7)

    def set_object_listbox(self):
        self.object_listbox.delete(0, tk.END)
        temp_list = self.db.get_object_list()
        element = ["" + str(record[0]) + " - " + record[1] for record in temp_list]
        self.object_listbox.insert(tk.END, *element)
        self.object_name_optionmenu.grid(row=3, column=7)

    def set_slide_listbox(self):
        self.slide_listbox.delete(0, tk.END)
        temp_list = self.db.get_slide_list()
        slide = ["" + str(record[1]) + " - " + record[2] for record in temp_list]
        self.slide_listbox.insert(tk.END, *slide)

    def run(self):
        detector = DataMatrixDetector(self.db)
        detector.set_template("../template.jpg")
        camera = Camera()
        camera.OnCapture += detector.detect_matrix
        camera.run()

if __name__ == "__main__":
    root = tk.Tk()
    root.wm_title("Interactive display")
    app = InteractiveDisplay(master=root)
    app.mainloop()
