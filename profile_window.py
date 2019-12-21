import tkinter as tk
from jcQueries import DataBase
import windows_init

def show_profile(main_user, user):
    def go_back():
        if main_user.type == "преподаватель":
            root.destroy()
            windows_init.show_teacher(main_user)
        elif main_user.type == "студент" and main_user.competence == "консультант":
            root.destroy()
            windows_init.show_consultant_window(main_user)
        else: #TODO: перейти на страницу диспетчера
            pass #TODO: перейти на страницу тьютора

    root = tk.Tk()
    root.resizable(False, False)
    root.title(user.name)
    screen_width = root.winfo_screenwidth() // 2 - 320 
    screen_height = root.winfo_screenheight() // 2 - 210 
    root.geometry('640x420+{}+{}'.format(screen_width, screen_height))

    db = DataBase()
    db.name = "postgres"      #TODO: delete this
    db.password = "postgres"  #TODO: delete this

    l_name = tk.Label(text="Имя: " + user.name)
    l_type = tk.Label(text="Тип: " + user.type)
    l_comp = tk.Label(text="Компетенция: " + user.competence)
    l_login = tk.Label(text="Логин: " + user.login)
    l_points = tk.Label()
    if main_user.type == "студент":
        l_points['text'] = "Баллы: " + user.points

    b_back = tk.Button(text="На главную", command=go_back)
    
    l_name.pack()
    l_type.pack()
    l_comp.pack()
    l_login.pack()
    l_points.pack()
    b_back.pack(side=tk.RIGHT)
    root.mainloop()