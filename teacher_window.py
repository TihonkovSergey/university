import tkinter as tk
from jcQueries import DataBase
import windows_init

def show_teacher(main_user):
    def show_users(event, users):
        lbox.delete(0,tk.END)
        for i in users:
            lbox.insert(0,i.name)
    def show_selected(event, users):
        label['text'] = ""
        select = list(lbox.curselection())
        if len(select):
            label['text'] = users[-select[0] -1].name
    def leave_akk(event, main_user):
        root.destroy()
        windows_init.show_login(main_user)
    
    root = tk.Tk()
    root.title("Авторизация")
    screen_width = root.winfo_screenwidth() // 2 - 320 
    screen_height = root.winfo_screenheight() // 2 - 210 
    root.geometry('640x420+{}+{}'.format(screen_width, screen_height))

    db = DataBase()
    b_show = tk.Button(text="Показать", compound=tk.TOP)
    b_get = tk.Button(text="Вывести выбранного")
    b_login = tk.Button(text="Выйти из аккаунта")
    label = tk.Label(bg='black', fg='white', width=40)
    lbox = tk.Listbox(width = 40, height = 10) 
    users_list = db.get_all_users()

    b_show.bind('<Button-1>', lambda event, users=users_list: show_users(event, users))
    b_get.bind('<Button-1>', lambda event, users=users_list: show_selected(event, users))
    b_login.bind('<Button-1>', lambda event, users=main_user: leave_akk(event, main_user))

    b_show.pack(side=tk.LEFT)
    b_get.pack(side=tk.LEFT)
    label.pack(side=tk.LEFT)
    lbox.pack(side=tk.LEFT)
    b_login.pack(side=tk.RIGHT)
    
    root.mainloop()