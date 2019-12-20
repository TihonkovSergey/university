import tkinter as tk
import windows_init
from jcQueries import DataBase

def show_my_students(main_user):
    def go_back():
        if main_user.type == "преподаватель":
            root.destroy()
            windows_init.show_teacher(main_user)
        elif main_user.type == "тьютор":
            pass #TODO: переход на страничку тьютора

    def show_students():
        lbox.delete(0,tk.END)
        students = []
        if var.get() == 0: #TODO: выбор сортированности 
            if var_order.get() == 0:
                students = db.get_all_students()
            elif var_order.get() == 1:
                students = db.get_students_order_by_points()
            else:
                sts = db.get_students_order_by_points()
                if not sts:
                    students = []
                else:
                    students=sts[::-1]
        elif var.get() == 1:
            if var_order.get() == 0:
                students = db.get_consultants()
            elif var_order.get() == 1:
                students = db.get_сonsultants_order_by_points()
            else:
                sts = db.get_сonsultants_order_by_points()
                if not sts:
                    students = []
                else:
                    students = sts[::-1]
        else:
            if var_order.get() == 0:
                students = db.get_dispatchers()
            elif var_order.get() == 1:
                students = db.get_dispatchers_order_by_points()
            else:
                sts = db.get_dispatchers_order_by_points()
                if not sts:
                    students = []
                else:
                    students = sts[::-1]
        if not students:
            lbox.insert(tk.END, "Ничего не найдено")
            students = []
        for st in students:
            lbox.insert(tk.END,st.name)
    
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
    b_back = tk.Button(text="Назад", command=go_back)
    lbox = tk.Listbox(width = 40, height = 10)

    r_all.pack()
    r_cons.pack()
    r_disp.pack()
    r_by_name.pack()
    r_by_p_u.pack()
    r_by_p_d.pack()
    b_show_students.pack(side="top")
    lbox.pack(side="top")
    b_back.pack(side=tk.RIGHT)

    root.mainloop()