import tkinter as tk
from jcQueries import DataBase
import windows_init

def show_admin(main_user):
    def leave_akk():
        root.destroy()
        windows_init.show_login(main_user)
    
    def show_students():
        root.destroy()
        windows_init.show_my_students(main_user)

    def show_my_profile():
        root.destroy()
        windows_init.show_my_profile(main_user)

    def show_teachers():
        root.destroy()
        windows_init.show_my_teachers_window(main_user)
    
    def add_users():
        pass #TODO: переход на диалоговое окно выбора файла для добавления новых пользователей
    
    root = tk.Tk()
    root.resizable(False, False)
    root.title("Добро пожаловать, админ " + main_user.name)
    
    screen_width = root.winfo_screenwidth() // 2 - 320 
    screen_height = root.winfo_screenheight() // 2 - 210 
    root.geometry('640x420+{}+{}'.format(screen_width, screen_height))

    db = DataBase()

    b_im = tk.Button(text="Мой профиль", command=show_my_profile)
    b_show_students  = tk.Button(text="Студенты", command=show_students)
    b_show_teachers = tk.Button(text="Преподаватели", command=show_teachers)
    b_add_users = tk.Button(text="Добавить пользователей сайта", command=add_users)
    b_login = tk.Button(text="Выйти из аккаунта", command=leave_akk)
    
    b_im.pack(side="top")
    b_show_students.pack(side="top")
    b_show_teachers.pack(side="top")
    b_add_users.pack(side="top")
    b_login.pack(side=tk.RIGHT)
    
    root.mainloop()