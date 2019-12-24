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
        #TODO: вывод преподавателей исходя из выбранной категории
    
    def show_profile():
        global curr_teachers
        select = list(lbox.curselection())
        if len(select) and curr_teachers:
            select_user = curr_teachers[select[0]]
            root.destroy()
            windows_init.show_profile(main_user, select_user)
        else:
            label['text'] = "Выберите преподавателя!"

    root = tk.Tk()
    root.resizable(False, False)
    root.title("Преподаватели")
    screen_width = root.winfo_screenwidth() // 2 - 320 
    screen_height = root.winfo_screenheight() // 2 - 210 
    root.geometry('640x420+{}+{}'.format(screen_width, screen_height))

    db = DataBase()

    b_show_teachers = tk.Button(text="Показать", compound=tk.TOP, command=show_teachers)
    b_show_profile = tk.Button(text="Посмотреть профиль", command=show_profile)
    b_back = tk.Button(text="Назад", command=go_back)
    lbox = tk.Listbox(width = 40, height = 10)
    label = tk.Label(width=40)

    b_show_teachers.pack(side="top")
    lbox.pack(side="top")
    b_show_profile.pack()
    label.pack()
    b_back.pack(side=tk.RIGHT)

    show_teachers()
    root.mainloop()