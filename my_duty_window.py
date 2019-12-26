import tkinter as tk
import windows_init
from jcQueries import DataBase
from tkinter import messagebox as mb

curr_duties = []

def show_my_duties(main_user):
    def go_back():
        if main_user.type == "преподаватель":
            root.destroy()
            windows_init.show_teacher(main_user)
        elif main_user.type == "тьютор":
            root.destroy()
            windows_init.show_tutor_window(main_user)
        else:
            root.destroy()
            windows_init.show_dispatcher_window(main_user)
    def show_duties():
        lbox.delete(0,tk.END)
        global curr_duties
        if var.get() == 0:
            #curr_duties = db.get_ TODO: для конкретного студента
            curr_duties = db.get_prev_duties()
        else: 
            # TODO: для конкретного студента
            curr_duties = db.get_next_duties()
        if not curr_duties:
            lbox.insert(tk.END, "Ничего не найдено")
            curr_duties = []

        for dut in curr_duties:
            user = db.get_user_by_id(dut.s_id)
            lbox.insert(tk.END, user.name + " " + dut.date)
    
    def add_duty():
        root.destroy()
        windows_init.show_add_duty(main_user)

    def change_der():
        global curr_duties
        select = list(lbox.curselection())
        if len(select) and curr_duties:
            select_duty = curr_duties[ select[0] ]
            root.destroy()
            windows_init.show_change_dispatcher_window(main_user, select_duty)
        else:
            mb.showerror("Ошибка","Выберите дежурство!")


    root = tk.Tk()
    root.resizable(False, False)
    root.title("Мои дежурства")
    screen_width = root.winfo_screenwidth() // 2 - 320 
    screen_height = root.winfo_screenheight() // 2 - 210 
    root.geometry('640x420+{}+{}'.format(screen_width, screen_height))

    db = DataBase()

    var = tk.IntVar()
    var.set(1)
    r_prev = tk.Radiobutton(text="Прошедшие", variable=var, value=0)
    r_curr = tk.Radiobutton(text="Запланированные", variable=var, value=1)

    b_show_duties = tk.Button(text="Показать", compound=tk.TOP, command=show_duties)
    b_change_der = tk.Button(text="Изменить дежурство", command=change_der)
    b_add_duty = tk.Button(text="Добавить дежурство", command=add_duty)
    b_back = tk.Button(text="Назад", command=go_back)
    lbox = tk.Listbox(width = 40, height = 10)
    label = tk.Label(width=40)

    r_curr.pack()
    r_prev.pack()
    b_show_duties.pack(side="top")
    lbox.pack(side="top")
    if main_user.type == "тьютор":
        b_add_duty.pack()
        b_change_der.pack()
    label.pack()
    b_back.pack(side=tk.RIGHT)

    root.mainloop()