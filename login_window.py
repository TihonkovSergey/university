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
            elif user.type == "студент" and user.competence == "консультант":
                root.destroy()
                windows_init.show_consultant_window(main_user)
            elif user.type == "студент" and user.competence == "диспетчер":
                root.destroy()
                windows_init.show_dispatcher_window(main_user)
            elif user.type == "админ":
                root.destroy()
                windows_init.show_admin_window(main_user)
            elif user.type == "тьютор":
                root.destroy()
                windows_init.show_tutor_window(main_user)
            else:
                except_label['text'] = "Неизвестная роль!"
    root = tk.Tk()
    root.resizable(False, False)
    screen_width = root.winfo_screenwidth() // 2 - 200  # 2 - 150
    screen_height = root.winfo_screenheight() // 2 - 65  # 2 - 50
    root.geometry('400x130+{}+{}'.format(screen_width, screen_height))
    root.title("Авторизация")

    db = DataBase()

    enter_login = tk.Entry()
    enter_login.insert(0, main_user.login)
    enter_password = tk.Entry()
    b_enter = tk.Button(text="Войти", command=try_login)
    except_label = tk.Label(width=40)

    except_label['text'] = "Введите логин и пароль"

    enter_login.place(x=125, y=30,
                      width=150, height=25)
    enter_password.place(x=125, y=60,
                         width=150, height=25)
    b_enter.place(x=165, y=90,
                  width=70, height=30)
    except_label.pack(side="top")

    root.mainloop()
