import tkinter as tk
import windows_init
from jcQueries import DataBase
from tkinter import messagebox as mb

curr_teachers = []
curr_students = []

def add_cons_teach(main_user, case):
    def go_back():
        root.destroy()
        windows_init.show_case_window(main_user, case)
    
    def show_teachers():
        global curr_teachers
        comp = case.category
        curr_teachers = db.get_teachers_by_competence(comp)
        if not curr_teachers:
            t_lbox.insert(tk.END, "Не найдено подходящих кураторов")
            curr_teachers = []
        for t in curr_teachers:
            t_lbox.insert(tk.END, t.name)

    def show_student():
        global curr_students
        curr_students = db.get_сonsultants_order_by_points()
        if not curr_students:
            s_lbox.insert(tk.END, "Не найдено подходящих консультантов")
            curr_students = []
        for s in curr_students:
            s_lbox.insert(tk.END, s.name + " " + str(s.points)) 
    
    def ok():
        select_teachers = list(t_lbox.curselection())
        select_students = list(s_lbox.curselection())
        if len(select_teachers) < 1:
            mb.showerror("Ошибка", "Выберите куратора среди преподавателей")
            return
        
        if len(select_students) < 1:
            mb.showerror("Ошибка", "Выберите консультанта")
            return
        case.status = "ожидаются правки плана консультации"
        case.s_id = curr_students[select_students[0]].id
        case.t_id = curr_teachers[select_teachers[0]].id
        db.update_case_by_id(case)
        go_back()

    root = tk.Tk()
    root.resizable(False, False)
    root.title("Добавление исполнителей")
    screen_width = root.winfo_screenwidth() // 2 - 320 
    screen_height = root.winfo_screenheight() // 2 - 320 
    root.geometry('640x640+{}+{}'.format(screen_width, screen_height))

    db = DataBase()
    
    b_back = tk.Button(text="Назад", command=go_back)
    t_lbox = tk.Listbox(exportselection=0, width = 40, height = 10)
    s_lbox = tk.Listbox(exportselection=0, width = 40, height = 10)
    b_ok = tk.Button(text="OK", command=ok)

    t_lbox.pack(side="top")
    s_lbox.pack(side="top")
    b_ok.pack()
    b_back.pack(side=tk.RIGHT)

    show_teachers()
    show_student()
    root.mainloop()