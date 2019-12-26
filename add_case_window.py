import tkinter as tk
from jcQueries import DataBase
import windows_init
import numpy as np
from jcCaseClass import Case
from jcSupplicantClass import Supplicant
from tkinter import messagebox as mb
from tkinter import filedialog as fd 
from jcDocumentsClass import Document
import string

def add_case(main_user):
    def add():
        case = Case(("", "", "", "", "", "", "", "", "", ""))
        supp = Supplicant(("", "", ""))

        supp_name = e_sup_name.get()
        supp_tel_number = e_sup_tel_number.get()

        title = e_title.get()
        description = t_description.get(0.0, tk.END)

        if len(supp_name) < 6:
            mb.showerror("Ошибка", "Имя обратившегося должно быть длиннее 5 символов!")
            return

        for c in supp_name:
            if not (("a" <= c <= "z") or ("A" <= c <= "Z") or 
                    ("а" <= c <= "я") or ("А"<= c <= "Я") or c==" "):
                mb.showerror("Ошибка", "Имя обратившегося должно содержать только буквы!")
                return
        supp.name = supp_name

        for c in supp_tel_number:
            if not (("0" <= c <= "9") or (c == "-")):
                mb.showerror("Ошибка", "Телефонный номер должен содержать только цифры")
                return

        if len(supp_tel_number) < 6:
            mb.showerror("Ошибка", "Телефонный номер должен быть длиннее 5 символов!")
            return

        supp.telephone_number = supp_tel_number

        if len(title) < 6:
            mb.showerror("Ошибка", "Название должно быть длиннее 5 символов!")
            return
        case.title = title
        select_comp = list(lb_category.curselection())
        if len(select_comp):
            case.category = competence_list[select_comp[0]]
        else:
            mb.showerror("Ошибка", "Категория дела не выбрана!")
            return
        case.description = description
        case.dispatcher_id = main_user.id
        
        supp_id = str(db.insert_supplicant(supp))
        if supp_id.isdigit():
            case.supplicant_id = supp_id
        else:
            mb.showerror("Ошибка", "Ошибка в добавлении обратившегося! " + supp_id)
            return
        case_id = str(db.insert_case(case))
        if case_id.isdigit():
            if var_doc.get():
                file_name = fd.askopenfilename(filetypes=(("Text FILES", "*.txt"),
                                                        ("All files", "*.*") ))
                if not db.get_document_by_id(file_name):
                    if not file_name:
                        mb.showerror("Ошибка", "Вы не выбрали файл!")
                        return
                    file_path_list = file_name.split("/")
                    doc = Document((file_name, file_path_list[-1], case.case_id))
                    db.insert_document(doc)
                    go_back()
                else:
                    mb.showerror("Ошибка", "Один и тот же документ не может быть прикреплен к разным делам")
                    return
        else:
            mb.showerror("Ошибка", "Ошибка в добавлении дела! " + case_id)
            return
        go_back()
    
    def go_back():
        root.destroy()
        windows_init.show_dispatcher_window(main_user)

    competence_list = ["гражданское право", "трудовое право", "административное право", "жилищное право"]


    root = tk.Tk()
    root.resizable(False, False)
    root.title("Добавление нового дела")
    screen_width = root.winfo_screenwidth() // 2 - 320 
    screen_height = root.winfo_screenheight() // 2 - 320 
    root.geometry('640x640+{}+{}'.format(screen_width, screen_height))

    db = DataBase()

    label_sup_name =tk.Label(text="Имя обратившегося: ")
    e_sup_name = tk.Entry(width=50)

    label_sup_tel_number = tk.Label(text="Номер телефона обратившегося:")
    e_sup_tel_number = tk.Entry(width=50)

    e_title = tk.Entry(width=50)
    e_title.insert(0, "Дело №" + str(np.random.randint(1500)))

    lb_category = tk.Listbox()
    for r in competence_list:
        lb_category.insert(tk.END, r) 
    
    t_description = tk.Text(width=35, height=10)

    var_doc = tk.BooleanVar()
    var_doc.set(0)
    check_doc = tk.Checkbutton(text="Прикрепить документ", variable=var_doc, onvalue=1, offvalue=0)
    
    b_add = tk.Button(text="Добавить", command=add)
    b_back = tk.Button(text="Назад", command=go_back)
    
    label_sup_name.pack()
    e_sup_name.pack()

    label_sup_tel_number.pack()
    e_sup_tel_number.pack()

    e_title.pack()
    lb_category.pack()

    t_description.pack()
    
    check_doc.pack()

    b_add.pack(side="bottom")
    b_back.pack(side=tk.RIGHT)

    root.mainloop()

    #TODO: добавить поля для Supplicant, добавить проверку этих полей и пуш в базу