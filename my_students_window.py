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
            root.destroy()
            windows_init.show_admin_window(main_user)

    def show_students():
        lbox.delete(0, tk.END)
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
                    curr_students = sts[::-1]
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
            lbox.insert(tk.END, st.name + " " +
                        st.competence + " " + str(st.points))

    def add_points():
        global curr_students
        select = list(lbox.curselection())
        if len(select) and curr_students:
            select_user = curr_students[select[0]]
            root.destroy()
            windows_init.show_add_points_window(main_user, select_user)
        else:
            pass  # """"""

    def show_profile():
        global curr_students
        select = list(lbox.curselection())
        if len(select) and curr_students:
            select_user = curr_students[select[0]]
            root.destroy()
            windows_init.show_profile(main_user, select_user)
        else:
            pass  # """"""

    root = tk.Tk()
    root.resizable(False, False)
    root.title("Мои студенты")
    screen_width = root.winfo_screenwidth() // 2 - 380
    screen_height = root.winfo_screenheight() // 2 - 125
    root.geometry('760x250+{}+{}'.format(screen_width, screen_height))

    db = DataBase()

    var = tk.IntVar()
    var.set(0)
    r_all = tk.Radiobutton(text="Все студенты", variable=var, value=0)
    r_cons = tk.Radiobutton(text="Консультанты", variable=var, value=1)
    r_disp = tk.Radiobutton(text="Диспетчеры", variable=var, value=2)

    var_order = tk.IntVar()
    var_order.set(0)
    r_by_name = tk.Radiobutton(text="По имени", variable=var_order, value=0)
    r_by_p_u = tk.Radiobutton(
        text="По возрастанию баллов", variable=var_order, value=1)
    r_by_p_d = tk.Radiobutton(
        text="По убыванию баллов", variable=var_order, value=2)

    b_show_students = tk.Button(
        text="Показать", compound=tk.TOP, command=show_students)
    b_add_points = tk.Button(text="Добавить баллы", command=add_points)
    b_show_profile = tk.Button(text="Посмотреть профиль", command=show_profile)
    b_back = tk.Button(text="Назад", command=go_back)
    lbox = tk.Listbox(width=40, height=10)

    title = tk.Label()
    title['text'] = "Список студентов:"
    title.place(x=0, y=0, width=300, height=20)
    lbox.place(x=0, y=20, width=300, height=150)

    r_all.place(x=305, y=20,  width=220, height=20)
    r_cons.place(x=310, y=70,  width=220, height=20)
    r_disp.place(x=305, y=120,  width=220, height=20)

    r_by_name.place(x=510, y=20, width=220, height=20)
    r_by_p_u.place(x=550, y=70, width=220, height=20)
    r_by_p_d.place(x=545, y=120, width=220, height=20)

    b_show_students.place(x=500, y=180, width=100, height=30)

    b_show_profile.place(x=0, y=170, width=300, height=30)

    if main_user.type != "админ":
        b_add_points.place(x=0, y=200, width=300, height=30)

    # label.pack()
    b_back.place(x=0, y=230, width=40, height=20)

    show_students()
    root.mainloop()
