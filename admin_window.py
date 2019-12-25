import tkinter as tk
from jcQueries import DataBase
import windows_init
from tkinter import filedialog as fd 
from tkinter import messagebox as mb
import json
from jcUserClass import User

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
        file_name = fd.askopenfilename(filetypes=(("Json FILES", "*.json"),
                                                        ("All files", "*.*") ))
        if not file_name:
            mb.showerror("Ошибка", "Вы не выбрали файл!")
            return
        f = open(file_name)
        new_data = json.load(f)
        f.close()
        logs_str = ""
        for data in new_data["users"]:
            user = User((data["id"], data["name"], data["type"], data["competence"], data["login"], data["password"], data["personal_data"], data["points"]))
            error = db.insert_users([user])
            if error and error != None  and error != "None" and error != "null" and error != "none":
                logs_str += "\n" + "User " + user.name + " not added: " + str(error)
            else:
                logs_str += "\n" + "User " + user.name + " successful added in database"
        
        f_logs = open("D:/homeworks/university_databases/logs.txt", "w")
        f_logs.write(logs_str)
        f_logs.close()
    
    def insert_user():
        pass #TODO: переход на страницу заполнения данных

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
    b_insert_user = tk.Button(text="Добавить пользователя", command=insert_user)
    b_add_users = tk.Button(text="Добавить пользователей из файла", command=add_users)
    b_login = tk.Button(text="Выйти из аккаунта", command=leave_akk)
    
    b_im.pack(side="top")
    b_show_students.pack(side="top")
    b_show_teachers.pack(side="top")
    b_insert_user.pack(side="top")
    b_add_users.pack(side="top")
    b_login.pack(side=tk.RIGHT)
    
    root.mainloop()