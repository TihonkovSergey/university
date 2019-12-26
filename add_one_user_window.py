import tkinter as tk
from jcQueries import DataBase
import windows_init
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from jcUserClass import User


def add_one_user(main_user):
    def go_back():
        root.destroy()
        windows_init.show_admin_window(main_user)

    def add():
        user = User(("", "", "", "", "", "", "", "0.0"))
        name = e_name.get()
        if len(name) < 6:
            mb.showerror(
                "Ошибка", "Имя пользователя должно быть длиннее 5 символов!")
            return

        for c in name:
            if not (("a" <= c <= "z") or ("A" <= c <= "Z") or
                    ("а" <= c <= "я") or ("А" <= c <= "Я") or c == " "):
                mb.showerror(
                    "Ошибка", "Имя пользователя должно содержать только буквы!")
                return
        user.name = name

        login = e_login.get()
        u = db.get_user_by_login(login)
        if u and u.login != user.login:
            mb.showerror("Ошибка", "Данный логин уже существует!")
            return

        if len(login) < 4:
            mb.showerror("Ошибка", "Логин должен быть длиннее 4 символов!")
            return

        for c in login:
            if not (("a" <= c <= "z") or ("A" <= c <= "Z") or ("0" <= c <= "9")):
                mb.showerror(
                    "Ошибка", "Логин должен содержать только латинские буквы и цифры!")
                return
        user.login = login

        select_comp = list(lb_comp.curselection())
        if len(select_comp):
            if type_var.get():
                user.competence = t_competence_list[select_comp[0]]
                user.type = "преподаватель"
            else:
                user.competence = s_competence_list[select_comp[0]]
                user.type = "студент"
        else:
            mb.showerror("Ошибка", "Выберите компетенцию у пользователя!")
            return

        password = e_password.get()
        if len(password) < 4:
            mb.showerror("Ошибка", "Пароль должен быть длиннее 3 символов!")
            return
        user.password = password
        db.insert_users([user])
        go_back()

    def change():
        lb_comp.delete(0, tk.END)
        if type_var.get():
            for c in t_competence_list:
                lb_comp.insert(tk.END, c)
        else:
            for c in s_competence_list:
                lb_comp.insert(tk.END, c)

    root = tk.Tk()
    root.resizable(False, False)
    root.title("Добавление нового пользователя")

    screen_width = root.winfo_screenwidth() // 2 - 210
    screen_height = root.winfo_screenheight() // 2 - 100
    root.geometry('420x290+{}+{}'.format(screen_width, screen_height))

    s_competence_list = ["консультант", "диспетчер"]
    t_competence_list = ["гражданское право", "трудовое право",
                         "административное право", "жилищное право"]

    db = DataBase()

    fio_label = tk.Label(text="ФИО")
    fio_label.pack()

    e_name = tk.Entry(width=40)
    type_var = tk.IntVar()
    type_var.set(0)
    r_s = tk.Radiobutton(text="Студент", variable=type_var,
                         value=0, command=change)
    r_t = tk.Radiobutton(text="Преподаватель",
                         variable=type_var, value=1, command=change)

    lb_comp = tk.Listbox(width=40, height=4)
    change()
    label_login = tk.Label(text="Логин:")
    e_login = tk.Entry(width=40)
    label_password = tk.Label(text="Пароль")
    e_password = tk.Entry(width=40)

    b_back = tk.Button(text="Назад", command=go_back)
    b_add = tk.Button(text="Добавить", command=add)

    e_name.pack()

    r_s.pack()
    r_t.pack()
    lb_comp.pack()
    label_login.pack()
    e_login.pack()
    label_password.pack()
    e_password.pack()

    b_add.pack()
    b_back.place(x=0, y=270, width=40, height=20)
    root.mainloop()
