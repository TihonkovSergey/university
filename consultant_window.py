import tkinter as tk
from jcQueries import DataBase
import windows_init

def show_consultant(main_user):
    def leave_akk():
        root.destroy()
        windows_init.show_login(main_user)
    def show_my_cases():
        root.destroy()
        windows_init.show_my_cases(main_user)
    def show_my_profile():
        root.destroy()
        windows_init.show_my_profile(main_user)
    def show_my_points():
        root.destroy()
        windows_init.show_my_points_window(main_user)    
    root = tk.Tk()
    root.resizable(False, False)
    root.title("Добро пожаловать, консультант")
    screen_width = root.winfo_screenwidth() // 2 - 320 
    screen_height = root.winfo_screenheight() // 2 - 210 
    root.geometry('640x420+{}+{}'.format(screen_width, screen_height))

    db = DataBase()
    db.name = "postgres"      #TODO: delete this
    db.password = "postgres"  #TODO: delete this

    b_im = tk.Button(text="Мой профиль", command=show_my_profile)
    b_show_my_cases = tk.Button(text="Мои дела", command=show_my_cases)
    b_my_points = tk.Button(text="Мои баллы", command=show_my_points)
    b_login = tk.Button(text="Выйти из аккаунта", command=leave_akk)
    
    b_im.pack(side="top")
    b_show_my_cases.pack(side="top")
    b_my_points.pack(side="top")
    b_login.pack(side=tk.RIGHT)
    
    root.mainloop()