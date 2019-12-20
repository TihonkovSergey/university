import tkinter as tk
import windows_init
from jcQueries import DataBase


def show_my_students(main_user):
    db = DataBase()
    db.password = "postgres"
    def go_back():
        if main_user.type == "преподаватель":
            root.destroy()
            windows_init.show_teacher(main_user)
        elif main_user.type == "тьютор":
            pass #TODO: переход на страничку тьютора

    def show_students():
        lbox.delete(0,tk.END)
        students = []
        if True: # выбраны конс/дисп /оба 
            students = db.get_students() # ???
        elif True:
            pass
        for st in students:
            lbox.insert(0,st.name)
    
    root = tk.Tk()
    root.resizable(False, False)
    root.title("Мои студенты")
    screen_width = root.winfo_screenwidth() // 2 - 320 
    screen_height = root.winfo_screenheight() // 2 - 210 
    root.geometry('640x420+{}+{}'.format(screen_width, screen_height))

    db = DataBase()

    b_show_students = tk.Button(text="Показать", compound=tk.TOP, command=show_students)
    b_back = tk.Button(text="Назад", command=go_back)
    lbox = tk.Listbox(width = 40, height = 10)

    b_show_students.pack(side="top")
    b_back.pack(side=tk.RIGHT)

    root.mainloop()