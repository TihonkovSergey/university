import tkinter as tk
from jcQueries import DataBase
from jcUserClass import User
import windows_init

curr_points = []


def show_points(main_user):
    def refresh():
        lbox.delete(0, tk.END)
        global curr_points
        if main_user.type == "преподаватель":
            curr_points = db.get_points_event_by_t_id(main_user.id)
            if not curr_points:
                lbox.insert(tk.END, "Ничего не найдено")
                curr_points = []
            for c in curr_points:
                student = db.get_user_by_id(c.s_id)
                if not student:
                    student = User(("id", "неизвестный студент",
                                    "студент", "-", "-", "-", "", "0.0"))
                lbox.insert(tk.END, c.points + " " + student.name +
                            " " + c.reason + " " + c.date_time)
        else:
            curr_points = db.get_points_event_by_s_id(main_user.id)
            if not curr_points:
                lbox.insert(tk.END, "Ничего не найдено")
                curr_points = []
            for c in curr_points:
                teacher = db.get_user_by_id(c.t_id)
                if not teacher:
                    teacher = User(
                        ("id", "неизвестный преподаватель", "преподаватель", "-", "-", "-", "", "0.0"))
                lbox.insert(tk.END, c.points + " " + teacher.name +
                            " " + c.reason + " " + c.date_time)

    def go_back():
        if main_user.type == "преподаватель":
            root.destroy()
            windows_init.show_teacher(main_user)
        elif main_user.type == "тьютор":
            root.destroy()
            windows_init.show_tutor_window(main_user)
        elif main_user.type == "студент" and main_user.competence == "консультант":
            root.destroy()
            windows_init.show_consultant_window(main_user)
        elif main_user.type == "студент" and main_user.competence == "диспетчер":
            root.destroy()
            windows_init.show_dispatcher_window(main_user)
        else:  # какая-то ошибка
            root.destroy()
            windows_init.show_login(main_user)

    root = tk.Tk()
    root.resizable(False, False)
    root.title("История баллов")
    screen_width = root.winfo_screenwidth() // 2 - 265
    screen_height = root.winfo_screenheight() // 2 - 110
    root.geometry('530x220+{}+{}'.format(screen_width, screen_height))

    db = DataBase()
    b_refresh = tk.Button(text="Обновить", command=refresh)
    b_back = tk.Button(text="Назад", command=go_back)
    lbox = tk.Listbox(width=80, height=10)

    lbox.pack()
    b_refresh.pack()
    b_back.place(x=0, y=200, width=40, height=20)
    refresh()

    root.mainloop()
