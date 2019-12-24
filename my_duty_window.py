import tkinter as tk
import windows_init
from jcQueries import DataBase

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
            pass #TODO: переход на страничку диспетчера
    def show_duties():
        lbox.delete(0,tk.END)
        global curr_duties
        if var.get() == 0:
            pass
        elif var.get() == 1:
            pass
        else:
            pass
        if not curr_duties:
            lbox.insert(tk.END, "Ничего не найдено")
            curr_students = []
        for st in curr_duties:
            lbox.insert(tk.END,st.name + " " + str(st.points))
    
    def add_duty():
        global curr_duties
        select = list(lbox.curselection())
        if len(select) and curr_duties:
            select_duty = curr_duties[ select[0] ]
            root.destroy()
            windows_init.show_add_points_window(main_user, select_duty) #TODO: сменить на добавление дежурства
        else:
            label['text'] = "Выберите дежурство!"

    def del_duty():
        global curr_duties
        select = list(lbox.curselection())
        if len(select) and curr_duties:
            select_duty = curr_duties[ select[0] ]
            #TODO: вызвать удаление дежурства
            show_duties()
        else:
            label['text'] = "Выберите дежурство!"

    def change_der():
        global curr_duties
        select = list(lbox.curselection())
        if len(select) and curr_duties:
            select_duty = curr_duties[ select[0] ]
            root.destroy()
            #windows_init.show_add_points_window(main_user, select_duty) #TODO: добавить переход на изменение дежурного
        else:
            label['text'] = "Выберите дежурство!"


    root = tk.Tk()
    root.resizable(False, False)
    root.title("Мои дежурства")
    screen_width = root.winfo_screenwidth() // 2 - 320 
    screen_height = root.winfo_screenheight() // 2 - 210 
    root.geometry('640x420+{}+{}'.format(screen_width, screen_height))

    db = DataBase()

    var = tk.IntVar()
    var.set(0)
    r_all = tk.Radiobutton(text="Все", variable=var, value=0)
    r_prev = tk.Radiobutton(text="Прошедшие", variable=var, value=1)
    r_curr = tk.Radiobutton(text="Запланированные", variable=var, value=2)

    b_show_duties = tk.Button(text="Показать", compound=tk.TOP, command=show_duties)
    b_change_der = tk.Button(text="Изменить дежурного", command=change_der)
    b_add_duty = tk.Button(text="Добавить дежурство", command=add_duty)
    b_del_duty = tk.Button(text="Удалить дежурство", command=del_duty)
    b_back = tk.Button(text="Назад", command=go_back)
    lbox = tk.Listbox(width = 40, height = 10)
    label = tk.Label(width=40)

    r_all.pack()
    r_curr.pack()
    r_prev.pack()
    b_show_duties.pack(side="top")
    lbox.pack(side="top")
    if main_user.type == "тьютор":
        b_add_duty.pack()
        b_del_duty.pack()
    label.pack()
    b_back.pack(side=tk.RIGHT)

    root.mainloop()