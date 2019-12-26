import tkinter as tk
import windows_init
from jcQueries import DataBase
from tkinter import messagebox as mb 

curr_teachers = []


def show_my_teachers(main_user):
    def go_back():
        root.destroy()
        windows_init.show_admin_window(main_user)

    def show_teachers():
        lbox.delete(0, tk.END)
        global curr_teachers
        curr_teachers = []
        select = list(lb.curselection())
        if len(select):
            if competence_list[select[0]] == "Все":
                t = []
                for comp in competence_list[1:]:
                    t.append(db.get_teachers_by_competence(comp))
                for ans in t:
                    if ans != None and ans != "None" and ans != "null" and ans:
                        curr_teachers += ans
            else:
                curr_teachers = db.get_teachers_by_competence(
                    competence_list[select[0]])
        else:
            mb.showerror("Ошибка", "Выберите категорию!")
            return 
        if not curr_teachers:
            lbox.insert(tk.END, "Ничего не найдено")
            curr_teachers = []
        for t in curr_teachers:
            lbox.insert(tk.END, t.name)

    def show_profile():
        global curr_teachers
        select = list(lbox.curselection())
        if len(select) and curr_teachers:
            select_user = curr_teachers[select[0]]
            root.destroy()
            windows_init.show_profile(main_user, select_user)
        else:
            mb.showerror("Ошибка", "Выберите преподавателя!")
            return

    def del_teacher():
        global curr_teachers
        select = list(lbox.curselection())
        if len(select) and curr_teachers:
            select_teacher = curr_teachers[select[0]]
            db.delete_user_by_id(select_teacher)
            show_teachers()
            return
        else:
            mb.showerror("Ошибка", "Выберите преподавателя!")
            return

    root = tk.Tk()
    root.resizable(False, False)
    root.title("Преподаватели")
    screen_width = root.winfo_screenwidth() // 2 - 230
    screen_height = root.winfo_screenheight() // 2 - 125
    root.geometry('460x250+{}+{}'.format(screen_width, screen_height))

    competence_list = ["Все", "гражданское право",
                       "трудовое право", "административное право", "жилищное право"]

    db = DataBase()

    lb = tk.Listbox(height=len(competence_list))
    for r in competence_list:
        lb.insert(tk.END, r)

    b_show_teachers = tk.Button(
        text="Показать", compound=tk.TOP, command=show_teachers)
    b_show_profile = tk.Button(text="Посмотреть профиль", command=show_profile)
    b_del = tk.Button(text="Удалить", command=del_teacher)
    b_back = tk.Button(text="Назад", command=go_back)
    lbox = tk.Listbox(width=40, height=10)

    title = tk.Label()
    title['text'] = "Список преподавателей:"
    title.place(x=0, y=0, width=300, height=20)

    lbox.place(x=0, y=20, width=300, height=150)

    category_label = tk.Label(text="Выберите категорию:")
    category_label.place(x=305, y=0, width=150, height=30)

    lb.place(x=305, y=40, width=150, height=100)

    b_show_teachers.place(x=390, y=140, width=60, height=30)

    b_show_profile.place(x=0, y=170, width=300, height=30)

    b_del.place(x=0, y=200, width=300, height=30)

    b_back.place(x=0, y=230, width=40, height=20)

    #show_teachers()
    root.mainloop()
