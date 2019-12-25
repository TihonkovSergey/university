import tkinter as tk
from jcQueries import DataBase
import windows_init


def show_dispatcher(main_user):
    def leave_akk():
        root.destroy()
        windows_init.show_login(main_user)

    def show_my_profile():
        root.destroy()
        windows_init.show_my_profile(main_user)

    def show_my_duties():
        root.destroy()
        windows_init.show_my_duties(main_user)

    def show_my_points():
        root.destroy()
        windows_init.show_my_points_window(main_user)

    def show_add_case():
        root.destroy()
        windows_init.show_add_case_window(main_user)

    root = tk.Tk()
    root.resizable(False, False)
    root.title("Здравствуйте, диспетчер " + main_user.name)
    screen_width = root.winfo_screenwidth() // 2 - 210
    screen_height = root.winfo_screenheight() // 2 - 100
    root.geometry('420x200+{}+{}'.format(screen_width, screen_height))

    db = DataBase()

    b_im = tk.Button(text="Мой профиль", command=show_my_profile)
    b_my_duties = tk.Button(text="Мои дежурства", command=show_my_duties)
    b_my_points = tk.Button(text="Мои баллы", command=show_my_points)
    b_add_case = tk.Button(text="Добавить обращение", command=show_add_case)
    b_login = tk.Button(text="Выйти из аккаунта", command=leave_akk)

    b_im.place(x=0, y=0, width=420, height=40)
    b_my_duties.place(x=0, y=40, width=420, height=40)
    b_my_points.place(x=0, y=80, width=420, height=40)
    b_add_case.place(x=0, y=120, width=420, height=40)
    b_login.place(x=0, y=160, width=420, height=40)

    root.mainloop()
