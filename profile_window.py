import tkinter as tk
from jcQueries import DataBase
from tkinter import messagebox as mb
import windows_init

def show_profile(main_user, user):
    def save():
        name = e_name.get()
        if len(name) < 6:
            mb.showerror("Ошибка", "Имя должно быть длиннее 6 символов!")
            return
        for c in name:
            if not (("a" <= c <= "z") or ("A" <= c <= "Z") or 
                    ("а" <= c <= "я") or ("А"<= c <= "Я") or c==" "):
                mb.showerror("Ошибка", "Имя должно содержать только буквы!")
                return
        if main_user.type == "админ":
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
                    mb.showerror("Ошибка", "Логин должен содержать только латинские буквы и цифры!")
                    return
            user.login = login

        user.name = name
        
        select_comp = list(lb_comp.curselection())
        if len(select_comp):
            if user.type == "студент":
                user.competence = s_competence_list[select_comp[0]]
            else:
                user.competence = t_competence_list[select_comp[0]]

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
            windows_init.show_my_students(main_user)
        elif main_user.type == "студент" and main_user.competence == "диспетчер":
            root.destroy()
            windows_init.show_dispatcher_window(main_user)
        else:
            if user.type == "студент":
                root.destroy()
                windows_init.show_my_students(main_user)
            elif user.type == "преподаватель":
                root.destroy()
                windows_init.show_my_teachers_window(main_user)
            else:
                root.destroy()
                windows_init.show_admin_window(main_user)

    root = tk.Tk()
    root.resizable(False, False)
    root.title(user.name)
    screen_width = root.winfo_screenwidth() // 2 - 320 
    screen_height = root.winfo_screenheight() // 2 - 210 
    root.geometry('640x420+{}+{}'.format(screen_width, screen_height))

    t_competence_list = ["гражданское право", "трудовое право", "административное право", "жилищное право"]
    s_competence_list = ["консультант", "диспетчер"]
    db = DataBase()

    label_name = tk.Label(text="Имя: ")
    if (main_user.type == "админ"):
        e_name = tk.Entry(width=40)
        e_name.insert(0, user.name)
    else:
        l_name = tk.Label(text=user.name, width=40)
    
    label_type = tk.Label(text="Тип: ")
    l_type = tk.Label(text=user.type)

    label_comp = tk.Label(text="Компетенция: " + user.competence)
    if main_user.type == "админ":
        if user.type == "студент":
            lb_comp = tk.Listbox(height=len(s_competence_list))
            for r in s_competence_list:
                lb_comp.insert(tk.END, r)
        else:
            lb_comp = tk.Listbox(height=len(t_competence_list))
            for r in t_competence_list:
                lb_comp.insert(tk.END, r)
    else:
        l_comp = tk.Label(text=user.competence)

    label_login = tk.Label(text="Логин: ")
    if main_user.type == "админ":
        e_login  = tk.Entry(width=40)
        e_login.insert(0, user.login)
    else:
        l_login = tk.Label(text=user.login)
    
    l_points = tk.Label(text="Баллы: " + str(user.points))

    b_back = tk.Button(text="Назад", command=go_back)
    b_save = tk.Button(text="Сохранить и выйти", command=save)
    
    label_name.pack()
    if main_user.type == "админ": 
        e_name.pack()
    else:
        l_name.pack()
    
    label_type.pack()
    l_type.pack()
    
    label_comp.pack()
    if main_user.type == "админ":
        lb_comp.pack()
    else:
        l_comp.pack()
    
    label_login.pack()
    if main_user.type == "админ":
        e_login.pack()
    else:
        l_login.pack()
    
    if user.type == "студент":
        l_points.pack()
    
    if main_user.type == "админ":
        b_save.pack(side="bottom")
    
    b_back.pack(side=tk.RIGHT)

    root.mainloop()