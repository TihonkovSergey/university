import tkinter as tk
from jcQueries import DataBase
import windows_init


def show_tutor(main_user):
    def leave_akk():
        root.destroy()
        windows_init.show_login(main_user)

    def show_students():
        root.destroy()
        windows_init.show_my_students(main_user)

    def show_my_cases():
        root.destroy()
        windows_init.show_my_cases(main_user)

    def show_my_profile():
        root.destroy()
        windows_init.show_my_profile(main_user)

    def show_duty():
        root.destroy()
        windows_init.show_my_duties(main_user)

    root = tk.Tk()
    root.resizable(False, False)
    root.title("Добро пожаловать, тьютор " + main_user.name)

    screen_width = root.winfo_screenwidth() // 2 - 210
    screen_height = root.winfo_screenheight() // 2 - 100
    root.geometry('420x200+{}+{}'.format(screen_width, screen_height))

    db = DataBase()

    b_show_my_students = tk.Button(text="Мои студенты", command=show_students)
    b_im = tk.Button(text="Мой профиль", command=show_my_profile)
    b_show_my_cases = tk.Button(text="Мои дела", command=show_my_cases)
    b_login = tk.Button(text="Выйти из аккаунта", command=leave_akk)
    b_duty = tk.Button(text="Дежурства", command=show_duty)

    b_im.place(x=0, y=0, width=420, height=40)
    b_show_my_cases.place(x=0, y=40, width=420, height=40)
    b_show_my_students.place(x=0, y=80, width=420, height=40)
    b_duty.place(x=0, y=120, width=420, height=40)
    b_login.place(x=0, y=160, width=420, height=40)

    root.mainloop()
