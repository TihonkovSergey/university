import tkinter as tk
from jcQueries import DataBase
import windows_init

def show_case(main_user, case):
    def save():
        case.title = e_title.get()
        case.description = t_description.get(0.0, tk.END)
        db.update_case_by_id(case)
        go_back()
    
    def go_back():
        if main_user.type == "преподаватель":
            root.destroy()
            windows_init.show_teacher(main_user)
        elif main_user.type == "студент":
            pass #TODO: перейти на страницу студента
        else:
            pass #TODO: перейти на страницу тьютора
    
    def add_doc(): #TODO: добавить диалоговое окно с добавлением документа
        b_add_doc['text'] = "Добавляет документ"

    root = tk.Tk()
    root.resizable(False, False)
    root.title(case.title)
    screen_width = root.winfo_screenwidth() // 2 - 320 
    screen_height = root.winfo_screenheight() // 2 - 210 
    root.geometry('640x420+{}+{}'.format(screen_width, screen_height))

    db = DataBase()
    db.name = "postgres"      #TODO: delete this
    db.password = "postgres"  #TODO: delete this

    e_title = tk.Entry(width=50)
    e_title.insert(0, case.title)

    l_category = tk.Label(text="Категория: " + case.category)
    l_description = tk.Label()
    l_description['text'] = "Описание: "
    t_description = tk.Text(width=35, height=10)
    t_description.insert(0.0, case.description)
    
    l_st = tk.Label(width=40)
    if case.s_id and case.s_id != "None" and case.s_id != "null":
        st = db.get_user_by_id(case.s_id)
        l_st['text'] ="Консультант: " + st.name
    else:
        l_st['text'] = "Консультант не назначен"

    l_t = tk.Label(width=40)
    if case.t_id and case.t_id != "None" and case.t_id != "null":
        t = db.get_user_by_id(case.t_id)
        l_t['text'] ="Куратор: " + t.name
    else:
        l_t['text'] = "Куратор не назначен"

    l_status = tk.Label(width=40)
    l_status['text'] = case.status

    l_sup = tk.Label(width=40)
    if case.supplicant_id and case.supplicant_id != "None" and case.supplicant_id != "null":
        sup = db.get_supplicant_by_id(case.supplicant_id)
        l_sup['text'] ="Заявитель: " + sup.name
    else:
        l_sup['text'] = "Заявитель не определен"

    l_disp = tk.Label(width=40)
    if case.dispatcher_id and case.dispatcher_id != "None" and case.dispatcher_id != "null":
        disp = db.get_user_by_id(case.dispatcher_id)
        l_disp['text'] = "Оператор: " + disp.name
    else:
        l_disp['text'] = "Оператор не определен"
    
    l_last_update = tk.Label(width=40)
    l_last_update['text'] = "Последнее изменение: " + case.last_update[:min(10,len(case.last_update))]

    b_add_doc = tk.Button(text="Прикрепить документ", command=add_doc)
    b_save = tk.Button(text="Сохранить и выйти", command=save)
    b_back = tk.Button(text="На главную", command=go_back)
    
    e_title.pack()
    l_category.pack()
    l_description.pack()
    t_description.pack()
    l_st.pack()
    l_t.pack()
    l_sup.pack()
    l_disp.pack()
    l_last_update.pack()
    
    b_add_doc.pack()
    b_save.pack(side="bottom")
    b_back.pack(side=tk.RIGHT)

    root.mainloop()