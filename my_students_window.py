import tkinter as tk
import windows_init
from jcQueries import DataBase

curr_students = []

def show_my_students(main_user):
    def go_back():
        if main_user.type == "преподаватель":
            root.destroy()
            windows_init.show_teacher(main_user)
        elif main_user.type == "тьютор":
            root.destroy()
            windows_init.show_tutor_window(main_user)
        else:
            pass #TODO: переход на страничку консультанта/диспетчера
    def show_students():
        lbox.delete(0,tk.END)
        global curr_students
        if var.get() == 0:
            if var_order.get() == 0:
                curr_students = db.get_all_students()
            elif var_order.get() == 1:
                curr_students = db.get_students_order_by_points()
            else:
                sts = db.get_students_order_by_points()
                if not sts:
                    curr_students = []
                else:
                    curr_students=sts[::-1]
        elif var.get() == 1:
            if var_order.get() == 0:
                curr_students = db.get_consultants()
            elif var_order.get() == 1:
                curr_students = db.get_сonsultants_order_by_points()
            else:
                sts = db.get_сonsultants_order_by_points()
                if not sts:
                    curr_students = []
                else:
                    curr_students = sts[::-1]
        else:
            if var_order.get() == 0:
                curr_students = db.get_dispatchers()
            elif var_order.get() == 1:
                curr_students = db.get_dispatchers_order_by_points()
            else:
                sts = db.get_dispatchers_order_by_points()
                if not sts:
                    curr_students = []
                else:
                    curr_students = sts[::-1]
        if not curr_students:
            lbox.insert(tk.END, "Ничего не найдено")
            curr_students = []
        for st in curr_students:
            lbox.insert(tk.END,st.name + " " + str(st.points))
    
    def add_points():
        global curr_students
        select = list(lbox.curselection())
        if len(select) and curr_students:
            select_user = curr_students[ select[0] ]
            root.destroy()
            windows_init.show_add_points_window(main_user, select_user)
        else:
            label['text'] = "Выберите студента!"
    
    def show_profile():
        global curr_students
        select = list(lbox.curselection())
        if len(select) and curr_students:
            select_user = curr_students[select[0]]
            root.destroy()
            windows_init.show_profile(main_user, select_user)
        else:
            label['text'] = "Выберите студента!"

    root = tk.Tk()
    root.resizable(False, False)
    root.title("Мои студенты")
    screen_width = root.winfo_screenwidth() // 2 - 320 
    screen_height = root.winfo_screenheight() // 2 - 210 
    root.geometry('640x420+{}+{}'.format(screen_width, screen_height))

    db = DataBase()
    db.name = "postgres"      #TODO: delete this
    db.password = "postgres"  #TODO: delete this

    var = tk.IntVar()
    var.set(0)
    r_all = tk.Radiobutton(text="Все студенты", variable=var, value=0)
    r_cons = tk.Radiobutton(text="Консультанты", variable=var, value=1)
    r_disp = tk.Radiobutton(text="Диспетчеры", variable=var, value=2)

    var_order = tk.IntVar()
    var_order.set(0)
    r_by_name = tk.Radiobutton(text="По имени", variable=var_order, value=0)
    r_by_p_u = tk.Radiobutton(text="По возрастанию баллов", variable=var_order, value=1)
    r_by_p_d = tk.Radiobutton(text="По убыванию баллов", variable=var_order, value=2)

    b_show_students = tk.Button(text="Показать", compound=tk.TOP, command=show_students)
    b_add_points = tk.Button(text="Добавить баллы", command=add_points)
    b_show_profile = tk.Button(text="Посмотреть профиль", command=show_profile)
    b_back = tk.Button(text="Назад", command=go_back)
    lbox = tk.Listbox(width = 40, height = 10)
    label = tk.Label(width=40)

    r_all.pack()
    r_cons.pack()
    r_disp.pack()
    r_by_name.pack()
    r_by_p_u.pack()
    r_by_p_d.pack()
    b_show_students.pack(side="top")
    lbox.pack(side="top")
    b_add_points.pack()
    b_show_profile.pack()
    label.pack()
    b_back.pack(side=tk.RIGHT)

    root.mainloop()