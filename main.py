import tkinter as tk
import windows_init
from jcQueries import DataBase
from tkinter import ttk
from tkinter import filedialog as fd
from jcUserClass import User


if __name__ == "__main__":
    main_user = User(("id", "name", "type", "comp", "login", "password", "pd"))
    
    windows_init.show_login(main_user)

    """
    root = tk.Tk()
    log_win = LoginWindow(root, main_user)
    next_win = TeacherWindow(log_win, main_user)
    log_win.pack()
    root.title("")
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    root.mainloop()"""