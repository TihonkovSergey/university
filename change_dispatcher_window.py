import tkinter as tk
import windows_init
from jcQueries import DataBase
from tkinter import messagebox as mb
from tkcalendar import DateEntry
from jcDutyClass import Duty
import datetime

curr_students = []


def change_disp(main_user, duty):
    def go_back():
        root.destroy()
        windows_init.show_my_duties(main_user)

    def ok():
        date = e_date.get_date()
        select = list(t_lbox.curselection())
        if len(select) > 0 and curr_students:
            duty.s_id = curr_students[select[0]].id
        selected_s = curr_students[select[0]]
        duty.date = date
        db.update_duty_by_id(duty)
        go_back()

    def delete():
        db.delete_duty_by_id(duty.duty_id)
        go_back()

    root = tk.Tk()
    root.resizable(False, False)
    root.title("Изменение дежурства")
    screen_width = root.winfo_screenwidth() // 2 - 210
    screen_height = root.winfo_screenheight() // 2 - 135
    root.geometry('420x270+{}+{}'.format(screen_width, screen_height))

    db = DataBase()
    b_del = tk.Button(text="Удалить дежурство", command=delete)
    b_back = tk.Button(text="Назад", command=go_back)
    t_lbox = tk.Listbox(exportselection=0, width=40, height=10)

    global curr_students
    curr_students = db.get_dispatchers()
    if not curr_students:
        t_lbox.insert(tk.END, "Нет диспетчеров")
        curr_students = []
    else:
        for s in curr_students:
            t_lbox.insert(tk.END, s.name)

    b_ok = tk.Button(text="OK", command=ok)
    e_date = DateEntry(root, width=12, background='darkblue',
                       foreground='white', borderwidth=2, year=2019)
    e_date.pack(padx=10, pady=10)
    t_lbox.pack(side="top")
    b_ok.pack()
    b_del.pack()
    b_back.place(x=0, y=250, width=40, height=20)
    root.mainloop()
