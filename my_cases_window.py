import tkinter as tk
from jcQueries import DataBase
import windows_init

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
            label['text'] = "Выберите дело!"
    root = tk.Tk()
    root.resizable(False, False)
    root.title("Мои дела")
    screen_width = root.winfo_screenwidth() // 2 - 320 
    screen_height = root.winfo_screenheight() // 2 - 210 
    root.geometry('640x420+{}+{}'.format(screen_width, screen_height))

    db = DataBase()

    b_all_cases = tk.Button(text="Все дела", compound=tk.TOP, command=show_all)
    b_check_cases = tk.Button(text="Требующие подтверждения дела", command=show_check)
    if main_user.type == "студент":
        b_check_cases = tk.Button(text="Требующие доработки дела")
    b_finished_cases = tk.Button(text="Завершенные дела", command=show_finished)
    b_back = tk.Button(text="Назад", command=go_back)
    lbox = tk.Listbox(width = 40, height = 10)
    b_case_win = tk.Button(text="Просмотреть выбранное дело", command=show_case_win)
    label = tk.Label(width=40)

    b_all_cases.pack()
    b_check_cases.pack()
    b_finished_cases.pack()
    lbox.pack()
    b_case_win.pack()
    label.pack()
    b_back.pack(side=tk.RIGHT)

    show_all()
    root.mainloop()