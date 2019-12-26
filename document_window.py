import tkinter as tk
from jcQueries import DataBase
import windows_init
from tkinter import messagebox as mb
from tkinter import filedialog as fd
from jcDocumentsClass import Document


def show_document(main_user, case, doc):
    def go_back():
        root.destroy()
        windows_init.show_case_window(main_user, case)

    def save():
        t = text.get(0.0, tk.END)
        f = open(doc.document_id, "w")
        f.write(t)
        f.close()
        go_back()

    root = tk.Tk()
    root.resizable(False, False)
    root.title("Документ " + doc.title)
    screen_width = root.winfo_screenwidth() // 2 - 320
    screen_height = root.winfo_screenheight() // 2 - 210
    root.geometry('640x400+{}+{}'.format(screen_width, screen_height))

    text = tk.Text(width=50, height=20)
    f = open(doc.document_id, "r")
    curr_text = f.read()
    f.close()
    text.insert(0.0, curr_text)

    b_save = tk.Button(text="Сохранить и выйти", command=save)
    b_back = tk.Button(text="Назад", command=go_back)

    text.pack()
    b_save.pack()
    b_back.place(x=0, y=380, width=40, height=20)
    root.mainloop()
