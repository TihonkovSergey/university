import tkinter as tk
from jcQueries import DataBase
import windows_init
from tkinter import messagebox as mb
from tkinter import filedialog as fd
from jcDocumentsClass import Document
from jcPointsEventClass import PointsEvent

curr_docs = []

def show_case(main_user, case):
    def save():
        case.title = e_title.get()
        case.description = t_description.get(0.0, tk.END)
        db.update_case_by_id(case)
        go_back()
    
    def go_back():
        root.destroy()
        windows_init.show_my_cases(main_user)

    def confirm():
        curr_status = case.status
        if curr_status == "ожидаются правки плана консультации":
            case.status = "ожидается проверка правок плана консультации"
        elif curr_status == "ожидаются правки резолюции":
            case.status = "ожидается проверка правок резолюции"
        elif curr_status == "ожидается проверка правок плана консультации":
            case.status = "ожидаются правки резолюции"
        else:
            case.status = "завершено"
            points_event = PointsEvent(("", "", "", "", "", ""))
            points_event.points = "1.0"
            points_event.s_id = case.s_id
            points_event.t_id = main_user.id
            points_event.reason = "завершение дела"
            db.insert_points_event([points_event])
            user = db.get_user_by_id(case.s_id)
            user.points = user.points + 1.0
            db.update_user_by_id(user)
            
        db.update_case_by_id(case)
        root.destroy()
        windows_init.show_case_window(main_user, case)
    
    def add_doc():
        file_name = fd.askopenfilename(filetypes=(("Text FILES", "*.txt"),
                                                        ("All files", "*.*") ))
        if not db.get_document_by_id(file_name):
            if not file_name:
                mb.showerror("Ошибка", "Вы не выбрали файл!")
                return
            file_path_list = file_name.split("/")
            doc = Document((file_name, file_path_list[-1], case.case_id))
            error = db.insert_document(doc)
            refresh_docs()
        else:
            mb.showerror("Ошибка", "Один и тот же документ не может быть прикреплен к разным делам")
            return

    def refresh_docs():
        lb_docs.delete(0, tk.END)
        global curr_docs
        curr_docs = db.get_documents_by_case_id(case.case_id)
        if not curr_docs:
            lb_docs.insert(tk.END, "Нет документов")
            curr_docs = []
        for d in curr_docs:
            lb_docs.insert(tk.END, d.title)

    def add_cons_teach():
        root.destroy()
        windows_init.show_add_cons_teach_window(main_user, case)

    def open_doc():
        global curr_docs
        select = list(lb_docs.curselection())
        if len(select) and curr_docs:
            select_doc = curr_docs[select[0]]
        else:
            mb.showerror("Ошибка","Выберите документ")
            return
        root.destroy()
        windows_init.show_document_window(main_user, case, select_doc)
    
    def delete_doc():
        global curr_docs
        select = list(lb_docs.curselection())
        if len(select) and curr_docs:
            select_doc = curr_docs[ select[0] ]
        else:
            mb.showerror("Ошибка","Выберите документ")
            return
        db.delete_document_by_id(select_doc.document_id)
        refresh_docs()

    root = tk.Tk()
    root.resizable(False, False)
    root.title(case.title)
    screen_width = root.winfo_screenwidth() // 2 - 320 
    screen_height = root.winfo_screenheight() // 2 - 420 
    root.geometry('640x840+{}+{}'.format(screen_width, screen_height))

    db = DataBase()

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

    l_status = tk.Label(text="Статус: " + case.status)

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

    
    if ((main_user.type == "студент")
            and (case.status == "ожидаются правки плана консультации" 
            or case.status == "ожидаются правки резолюции")):
        b_confirm = tk.Button(text="Отправить на проверку", command=confirm)
    elif main_user.type == "тьютор" and case.status == "ожидает назначения ответственных":
        b_confirm = tk.Button(text="Назначить консультанта и куратора", command=add_cons_teach)
    else:
        b_confirm = tk.Button(text="Принять правки", command=confirm)

    lb_docs = tk.Listbox(width = 40, height = 10)

    b_add_doc = tk.Button(text="Прикрепить документ", command=add_doc)
    b_open_doc = tk.Button(text="Открыть документ", command=open_doc)
    b_del_doc = tk.Button(text="Удалить документ", command=delete_doc)
    b_save = tk.Button(text="Сохранить и выйти", command=save)
    b_back = tk.Button(text="Назад", command=go_back)
    
    e_title.pack()
    l_category.pack()
    l_description.pack()
    t_description.pack()
    l_st.pack()
    l_t.pack()
    l_status.pack()
    l_sup.pack()
    l_disp.pack()
    l_last_update.pack()
 
    b_confirm.pack()
    
    lb_docs.pack()

    b_add_doc.pack()
    b_open_doc.pack()
    b_del_doc.pack()
    b_save.pack(side="bottom")
    b_back.pack(side=tk.RIGHT)

    refresh_docs()
    root.mainloop()