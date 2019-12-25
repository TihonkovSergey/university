import tkinter as tk
import windows_init
from jcQueries import DataBase

curr_teachers = []

def show_my_teachers(main_user):
    def go_back():
        root.destroy()
        windows_init.show_admin_window(main_user)
    
    def show_teachers():
        lbox.delete(0,tk.END)
        global curr_teachers
        curr_teachers = []
        select = list(lb.curselection())
        if len(select):
            if competence_list[select[0]] == "Все":
                t = []
                for comp in competence_list[1:]:
                    t.append(db.get_teachers_by_competence(comp))
                for ans in t:
                    if ans != None and ans != "None" and ans != "null" and ans:
                        curr_teachers += ans
            else:
                curr_teachers = db.get_teachers_by_competence(competence_list[select[0]])
        else:
            label['text'] = "Выберите категорию"
        if not curr_teachers:
            lbox.insert(tk.END, "Ничего не найдено")
            curr_teachers = []
        for t in curr_teachers:
            lbox.insert(tk.END, t.name)
    
    def show_profile():
        global curr_teachers
        select = list(lbox.curselection())
        if len(select) and curr_teachers:
            select_user = curr_teachers[select[0]]
            root.destroy()
            windows_init.show_profile(main_user, select_user)
        else:
            label['text'] = "Выберите преподавателя!"

    def del_teacher():
        global curr_teachers
        select = list(lbox.curselection())
        if len(select) and curr_teachers:
            select_teacher = curr_teachers[ select[0] ]
            db.delete_user_by_id(select_teacher)
            show_teachers()
            return
        else:
            label['text'] = "Выберите преподавателя!"


    root = tk.Tk()
    root.resizable(False, False)
    root.title("Преподаватели")
    screen_width = root.winfo_screenwidth() // 2 - 320 
    screen_height = root.winfo_screenheight() // 2 - 210 
    root.geometry('640x420+{}+{}'.format(screen_width, screen_height))

    competence_list = ["Все", "гражданское право", "трудовое право", "административное право", "жилищное право"]

    db = DataBase()
    
    lb = tk.Listbox(height=len(competence_list))
    for r in competence_list:
        lb.insert(tk.END, r)
            

    b_show_teachers = tk.Button(text="Показать", compound=tk.TOP, command=show_teachers)
    b_show_profile = tk.Button(text="Посмотреть профиль", command=show_profile)
    b_del = tk.Button(text="Удалить", command=del_teacher)
    b_back = tk.Button(text="Назад", command=go_back)
    lbox = tk.Listbox(width = 40, height = 10)
    label = tk.Label(width=40)

    lb.pack()
    b_show_teachers.pack(side="top")
    lbox.pack(side="top")
    b_show_profile.pack()
    b_del.pack(side="top")
    label.pack()
    b_back.pack(side=tk.RIGHT)

    show_teachers()
    root.mainloop()