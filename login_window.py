import tkinter as tk
from jcQueries import DataBase
import windows_init

def show_login(main_user):
    def try_login():
        login = enter_login.get()
        password = enter_password.get()
        user = db.get_user_by_login(login)
        if (login == ""):
            except_label['text'] = "Введите логин"
            return
        if (login != "" and password == ""):
            except_label['text'] = "Введите пароль"
            return
        if (not user):
            except_label['text'] = 'Несуществующий логин'
        elif user.password != password:
            except_label['text'] = 'Неверный пароль'
        else:
            except_label['text'] = 'Успешно'
            main_user = user
            if user.type == 'преподаватель':
                root.destroy()
                windows_init.show_teacher(main_user)
    root = tk.Tk()
    screen_width = root.winfo_screenwidth() // 2 - 150 
    screen_height = root.winfo_screenheight() // 2 - 50 
    root.geometry('300x100+{}+{}'.format(screen_width, screen_height))
    root.title("Авторизация")
    
    db = DataBase()
    enter_login = tk.Entry()
    enter_password = tk.Entry()
    b_enter = tk.Button(text="Войти", command=try_login)
    except_label = tk.Label(width=40)

    enter_login.pack(side="top")
    enter_password.pack(side="top")
    b_enter.pack(side="top")
    except_label.pack(side="top")

    root.mainloop()