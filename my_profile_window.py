import tkinter as tk
from jcQueries import DataBase
import windows_init
from tkinter import messagebox as mb 

def show_my_profile(main_user):
    def save():
        if main_user.type == "админ":
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
        password = e_password.get()
        if len(password) < 4:
            mb.showerror("Ошибка", "Пароль должен быть длиннее 3 символов!")
            return
        user.password = password
        db.update_user_by_id(main_user)
        go_back()

    def go_back():
        if main_user.type == "преподаватель":
            root.destroy()
            windows_init.show_teacher(main_user)
        elif main_user.type == "студент" and main_user.competence == "консультант":
            root.destroy()
            windows_init.show_consultant_window(main_user)
        elif main_user.type == "тьютор":
            root.destroy()
            windows_init.show_tutor_window(main_user)
        elif main_user.type == "студент" and main_user.competence == "диспетчер":
            root.destroy()
            windows_init.show_dispatcher_window(main_user)
        else:
            root.destroy()
            windows_init.show_admin_window(main_user)

    root = tk.Tk()
    root.resizable(False, False)
    root.title("Мой профиль")
    screen_width = root.winfo_screenwidth() // 2 - 210
    screen_height = root.winfo_screenheight() // 2 - 120
    root.geometry('420x235+{}+{}'.format(screen_width, screen_height))

    db = DataBase()

    if (main_user.type == "админ"):
        e_name_text = tk.Label(width=40)
        e_name_text['text'] = "Изменить ФИО:"
        e_name_text.pack(side="top")

        e_name = tk.Entry(width=40)
        e_name.insert(0, main_user.name)
    else:
        l_nm = tk.Label(width=40)
        l_nm['text'] = "ФИО:"
        l_nm.pack(side="top")

        l_name = tk.Label(width=40)
        l_name['text'] = main_user.name
        l_name.pack(side="top")

    l_comp = tk.Label(text=main_user.competence)
    l_login = tk.Label(text=main_user.login)
    e_password = tk.Entry(width=20)
    e_password.insert(0, main_user.password)

    l_points = tk.Label()
    if main_user.type == "студент":
        l_points['text'] = main_user.points

    b_save = tk.Button(text="Сохранить и выйти", command=save)
    b_back = tk.Button(text="Назад", command=go_back)

    if main_user.type == "админ":
        e_name.pack()
    else:
        l_name.pack()

    if main_user.type == "студент" or main_user.type == "преподаватель":
        l_comp_text = tk.Label(width=40)
        l_comp_text['text'] = "КОМПЕТЕНЦИЯ:"
        l_comp_text.pack(side="top")

        l_comp.pack(side="top")

    if main_user.type == "студент":
        l_points_text = tk.Label(width=40)
        l_points_text['text'] = "МОИ БАЛЛЫ:"
        l_points_text.pack(side="top")
        l_points.pack(side="top")

    if main_user.type == "студент" or main_user.type == "преподаватель":
        l_login_text = tk.Label(width=40)
        l_login_text['text'] = "ЛОГИН:"
        l_login_text.pack(side="top")

        l_login.pack(side="top")

    if main_user.type == ("админ"):
        e_login_text = tk.Label(width=40)
        e_login_text['text'] = "Изменить логин:"
        e_login_text.pack(side="top")

        e_login = tk.Entry(width=40)
        e_login.insert(0, main_user.login)
        e_login.pack(side="top")

    e_password_text = tk.Label(width=40)
    e_password_text['text'] = "Изменить пароль:"
    e_password_text.pack(side="top")

    e_password.pack(side="top")
    b_save.pack(side="top")

    b_back.place(x=0, y=210, width=60, height=25)

    root.mainloop()
