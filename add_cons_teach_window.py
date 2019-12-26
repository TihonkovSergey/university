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
            case_number = 0
            t_cases = db.get_cases_by_teacher_id(t.id)
            if t_cases and t_cases != "None" and t_cases != "null":
                case_number = len(t_cases)
            t_lbox.insert(tk.END, t.name + " (" + str(case_number) + ")")

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
        if len(select_teachers) < 1 or not curr_teachers:
            mb.showerror("Ошибка", "Выберите куратора среди преподавателей")
            return

        if len(select_students) < 1 or not curr_students:
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
    screen_width = root.winfo_screenwidth() // 2 - 210
    screen_height = root.winfo_screenheight() // 2 - 135
    root.geometry('420x270+{}+{}'.format(screen_width, screen_height))

    db = DataBase()

    b_back = tk.Button(text="Назад", command=go_back)
    t_lbox = tk.Listbox(exportselection=0, width=40, height=5)
    s_lbox = tk.Listbox(exportselection=0, width=40, height=5)
    b_ok = tk.Button(text="OK", command=ok)

    curator_label = tk.Label(text="Выберите куратора дела")
    curator_label.pack()
    t_lbox.pack(side="top")

    student_label = tk.Label(text="Выберите консультанта по делу")
    student_label.pack()
    s_lbox.pack(side="top")

    b_ok.pack()
    b_back.place(x=0, y=250, width=40, height=20)

    show_teachers()
    show_student()
    root.mainloop()
