import tkinter as tk
from jcQueries import DataBase
import windows_init
from jcPointsEventClass import PointsEvent

def show_add_points(main_user, user):
    def go_back():
        root.destroy()
        windows_init.show_my_students(main_user)
    
    def add():  
        user.points = max(user.points + float(varAsTxt.get()), 0.0)
        db.update_user_by_id(user)
        points_event = PointsEvent(("id", varAsTxt.get(), user.id, main_user.id, var_reason.get(), ""))
        list_events = [ points_event ]
        db.insert_points_event(list_events)
        l_exp['text'] = varAsTxt.get()
        go_back()
    
    def onSelect(val):
        sender = val.widget
        idx = sender.curselection()
        value = sender.get(idx)   

        var_reason.set(value)

    root = tk.Tk()
    root.resizable(False, False)
    screen_width = root.winfo_screenwidth() // 2 - 150 
    screen_height = root.winfo_screenheight() // 2 - 150 
    root.geometry('300x300+{}+{}'.format(screen_width, screen_height))
    root.title("Добавление баллов")
    
    reason_list = ["Доклад"]
    if user.competence == "диспетчер":
        reason_list.append("Дежурство")
    else:
        reason_list.append("Завершенное дело")
    db = DataBase()

    varAsTxt = tk.StringVar()                    # an MVC-trick an indirect value-holder
    scale = tk.Scale(root,
                    variable   = varAsTxt,    # MVC-Model-Part value holder
                    from_      = -1.0,       # MVC-Model-Part value-min-limit
                    to         =  1.0,       # MVC-Model-Part value-max-limit
                    length     = 600,         # MVC-Visual-Part layout geometry [px]
                    digits     =   2,         # MVC-Visual-Part presentation trick
                    resolution =   0.1,
                    orient     = tk.HORIZONTAL       # MVC-Controller-Part stepping
                    )
        
    var_reason = tk.StringVar()
    lb = tk.Listbox(height=len(reason_list))
    for r in reason_list:
        lb.insert(tk.END, r)
            
    lb.bind("<<ListboxSelect>>", onSelect)     

    b_add = tk.Button(text="Отправить", command=add)
    b_back = tk.Button(text="Отмена", command=go_back)
    l_exp = tk.Label(width=40)

    scale.pack()
    lb.pack(pady=15)
    l_exp.pack()
    b_add.pack()
    b_back.pack(side=tk.RIGHT)

    root.mainloop()