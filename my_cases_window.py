import tkinter as tk
from jcQueries import DataBase
import windows_init
from tkinter import messagebox as mb 

curr_cases = []

def show_my_cases(main_user):
    def go_back():
        if main_user.type == "преподаватель":
            root.destroy()
            windows_init.show_teacher(main_user)
        elif main_user.type == "тьютор":
            root.destroy()
            windows_init.show_tutor_window(main_user)
        elif main_user.type == "студент":
            root.destroy()
            windows_init.show_consultant_window(main_user)
        else: # какая-то ошибка
            root.destroy()
            windows_init.show_login(main_user)
    def show_all():
        lbox.delete(0,tk.END)
        global curr_cases
        if main_user.type == "тьютор":
            curr_cases = db.get_all_cases()
        elif main_user.type == "преподаватель":
            curr_cases = db.get_cases_by_teacher_id(main_user.id)
        elif main_user.type == "студент": 
            curr_cases = db.get_cases_by_student_id(main_user.id)
        if not curr_cases:
            lbox.insert(tk.END, "Ничего не найдено")
            curr_cases = []
        for c in curr_cases:
            lbox.insert(tk.END,c.title)
    def show_check():
        lbox.delete(0,tk.END)
        global curr_cases
        if main_user.type == "тьютор":
            curr_cases = db.get_all_cases_waiting_for_appointment()
        elif main_user.type == "преподаватель":
            curr_cases = db.get_cases_which_need_teacher_editing(main_user.id)
        else:
            curr_cases = db.get_cases_which_need_student_editing(main_user.id)
        if not curr_cases:
            lbox.insert(tk.END, "Ничего не найдено")
            curr_cases = []
        for c in curr_cases:
            lbox.insert(tk.END,c.title)
    def show_finished():
        lbox.delete(0,tk.END)
        global curr_cases
        if main_user.type == "тьютор":
            pass
            curr_cases = db.get_all_completed_cases()
        elif main_user.type == "преподаватель":
            curr_cases = db.get_teacher_completed_cases(main_user.id)
        else:
            curr_cases = db.get_student_completed_cases(main_user.id)
        if not curr_cases:
            lbox.insert(tk.END, "Ничего не найдено")
            curr_cases = []
        for c in curr_cases:
            lbox.insert(tk.END,c.title)

    def show_case_win():
        global curr_cases
        select = list(lbox.curselection())
        if len(select) and curr_cases:
            select_case = curr_cases[select[0]]
            root.destroy()
            windows_init.show_case_window(main_user, select_case)
        else:
            mb.showerror("Ошибка", "Вы не выбрали дело!")
            return

    def change():
        if type_var.get() == 0:
            show_all()
        elif type_var.get() == 1:
            show_check()
        else:
            show_finished()

    root = tk.Tk()
    root.resizable(False, False)
    root.title("Мои дела")
    screen_width = root.winfo_screenwidth() // 2 - 320 
    screen_height = root.winfo_screenheight() // 2 - 210 
    root.geometry('640x420+{}+{}'.format(screen_width, screen_height))

    db = DataBase()

    type_var = tk.IntVar()
    type_var.set(0)
    
    r_all_cases = tk.Radiobutton(text="Все дела", variable=type_var, value=0, command=change)
    r_check_cases = tk.Radiobutton(text="Требующие подтверждения", variable=type_var, value=1, command=change)
    if main_user.type == "студент":
        r_check_cases = tk.Radiobutton(text="Требующие доработки", variable=type_var, value=1, command=change)
    r_finished_cases = tk.Radiobutton(text="Завершенные", variable=type_var, value=2, command=change)
    
    b_back = tk.Button(text="Назад", command=go_back)
    lbox = tk.Listbox(width = 40, height = 10)
    b_case_win = tk.Button(text="Просмотреть выбранное дело", command=show_case_win)
    
    change()
    
    r_all_cases.pack()
    r_check_cases.pack()
    r_finished_cases.pack()
    lbox.pack()
    b_case_win.pack()
    b_back.pack(side=tk.RIGHT)

    show_all()
    root.mainloop()