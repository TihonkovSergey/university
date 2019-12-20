import tkinter as tk
from jcQueries import DataBase
import windows_init

def show_my_cases(main_user):
    def show_all_cases(event):
        cases = get_cases_by_id() # ???
        lbox.delete(0,tk.END)
        for c in cases:
            lbox.insert(0,c.title)
    def show_check_cases(event):
        cases = []
        if main_user.type == "преподаватель":
            cases = get_cases_by_cat_for_id() # ???
        else:
            pass # ???

    root = tk.Tk()
    root.resizable(False, False)
    root.title("Мои дела")
    screen_width = root.winfo_screenwidth() // 2 - 320 
    screen_height = root.winfo_screenheight() // 2 - 210 
    root.geometry('640x420+{}+{}'.format(screen_width, screen_height))

    db = DataBase()
    b_all_cases = tk.Button(text="Показать", compound=tk.TOP)
    b_check_cases = tk.Button(text="Требующие подтверждения дела")
    if main_user.type == "студент":
        b_check_cases = tk.Button(text="Требующие доработки дела")
    b_finished_cases = tk.Button(text="Завершенные дела")
    b_back = tk.Button(text="Назад")
    lbox = tk.Listbox(width = 40, height = 10)

    b_all_cases.bind('<Button-1>', show_all_cases)
    b_check_cases.bind('<Button-1>', show_selected)
    b_finished_cases.bind('<Button-1>', )


    root.mainloop()