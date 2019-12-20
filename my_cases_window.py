import tkinter as tk
from jcQueries import DataBase
import windows_init

curr_cases = []

def show_my_cases(main_user):
    def go_back():
        if main_user.type == "преподаватель":
            root.destroy()
            windows_init.show_teacher(main_user)
        elif main_user.type == "тьютор":
            pass #TODO: переход на страничку тьютора
        else:
            pass #TODO: переход на страничку консультанта/диспетчера
    def show_all():
        lbox.delete(0,tk.END)
        global curr_cases
        if main_user.type == "тьютор":
            curr_cases = db.get_all_cases() # правильно?
        elif main_user.type == "преподаватель":
            curr_cases = db.get_cases_by_teacher_id(main_user.id)
        elif main_user.type == "студент": 
            curr_cases = db.get_cases_by_student_id(main_user.id)
        if not curr_cases:
            curr_cases = []
        for c in curr_cases:
            lbox.insert(0,c.title)
    def show_check():
        lbox.delete(0,tk.END)
        global curr_cases
        if main_user.type == "преподаватель":
            pass
            #cases = get_cases_by_cat_for_id() # ???
        else:
            pass # ???
    def show_finished():
        lbox.delete(0,tk.END)
        global curr_cases

    root = tk.Tk()
    root.resizable(False, False)
    root.title("Мои дела")
    screen_width = root.winfo_screenwidth() // 2 - 320 
    screen_height = root.winfo_screenheight() // 2 - 210 
    root.geometry('640x420+{}+{}'.format(screen_width, screen_height))

    db = DataBase()
    db.name = "postgres"      #TODO: delete this
    db.password = "postgres"  #TODO: delete this

    b_all_cases = tk.Button(text="Показать", compound=tk.TOP, command=show_all)
    b_check_cases = tk.Button(text="Требующие подтверждения дела", command=show_check)
    if main_user.type == "студент":
        b_check_cases = tk.Button(text="Требующие доработки дела")
    b_finished_cases = tk.Button(text="Завершенные дела", command=show_finished)
    b_back = tk.Button(text="Назад", command=go_back)
    lbox = tk.Listbox(width = 40, height = 10)

    b_all_cases.pack()
    b_check_cases.pack()
    b_finished_cases.pack()
    lbox.pack()
    b_back.pack(side=tk.RIGHT)

    root.mainloop()