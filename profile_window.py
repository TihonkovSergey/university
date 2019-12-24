import tkinter as tk
from jcQueries import DataBase
import windows_init

def show_profile(main_user, user):
    def save():
        user.name = e_name.get()
        db.update_user_by_id(user)
        go_back()
    
    def go_back():
        if main_user.type == "преподаватель":
            root.destroy()
            windows_init.show_my_students(main_user)
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
    root.title(user.name)
    screen_width = root.winfo_screenwidth() // 2 - 320 
    screen_height = root.winfo_screenheight() // 2 - 210 
    root.geometry('640x420+{}+{}'.format(screen_width, screen_height))

    db = DataBase()
    db.name = "postgres"      #TODO: delete this
    db.password = "postgres"  #TODO: delete this

    if (main_user.type == "админ"):
        e_name = tk.Entry(width=40)
        e_name.insert(0, user.name)
    else:
        l_name = tk.Label(width=40)
        l_name['text'] =  'Имя: ' + user.name
    
    l_type = tk.Label(text="Тип: " + user.type)
    l_comp = tk.Label(text="Компетенция: " + user.competence)
    l_login = tk.Label(text="Логин: " + user.login)
    l_points = tk.Label()
    if user.type == "студент":
        l_points['text'] = "Баллы: " + str(user.points)

    b_back = tk.Button(text="Назад", command=go_back)
    b_save = tk.Button(text="Сохранить и выйти", command=save)
    
    if main_user.type == "админ": 
        e_name.pack()
    else:
        l_name.pack()

    l_type.pack()
    l_comp.pack()
    l_login.pack()
    l_points.pack()
    if main_user.type == "админ":
        b_save.pack(side="bottom")
    b_back.pack(side=tk.RIGHT)
    root.mainloop()