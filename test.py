import psycopg2
from jcUserClass import User
from jcQuerys import *
from psycopg2 import sql
from tkinter import *
from tkinter import filedialog as fd


def update_user_by_id(user_id):
    conn = psycopg2.connect(dbname='postgres', user='postgres', password='postgres', host='localhost')
    with conn.cursor() as cursor:
        sql = """ UPDATE users
                    SET competence = %s
                    WHERE user_id = %s"""
        try:
            # execute the UPDATE  statement
            cursor.execute(sql, ('консультант', user_id))
            # get the number of updated rows
            conn.commit()
            # Close communication with the PostgreSQL database
            cursor.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)



def show_users(event, users):
    lbox.delete(0,END)
    for i in users:
        lbox.insert(0,i.name)

def get_and_update_choosen(event, users):
    label['text'] = ""
    select = list(lbox.curselection())
    if len(select):
        label['text'] = users[-select[0] -1].name
        #update_user_by_id(users[-select[0] -1].id)

users_list = get_all_users()

root = Tk()
#e = Entry(width=20)
b_show = Button(text="Показать")
b_get = Button(text="Вывести выбранного")

label = Label(bg='black', fg='white', width=40)
lbox = Listbox(width = 40, height = 10) 

def about():
    a = Toplevel()
    a.geometry('200x150')
    a['bg'] = 'grey'
    a.overrideredirect(True)
    Label(a, text="About this").pack(expand=1)
    a.after(5000, lambda: a.destroy())

def insert_text():
    file_name = fd.askopenfilename()
    f = open(file_name)
    s = f.read()
    text.insert(1.0, s)
    f.close()

def extract_text():
    file_name = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"),
                                        ("HTML files", "*.html;*.htm"),
                                                ("All files", "*.*") ))
    f = open(file_name, 'w')
    s = text.get(1.0, END)
    f.write(s)
    f.close()

text = Text()
text.grid(row=0)
b_show.bind('<Button-1>', lambda event, users=users_list: show_users(event, users))
b_get.bind('<Button-1>', lambda event, users=users_list: get_and_update_choosen(event, users))
b_insert = Button(text="Открыть", command=insert_text)
b_extract = Button(text="Сохранить", command=extract_text)

#e.pack()
b_show.grid(row=1)#b_show.pack()
b_get.grid(row=2)#b_get.pack()
label.grid(row=3)#label.pack()
lbox.grid(row=4)#lbox.pack()
b_insert.grid(row=5)
b_extract.grid(row=6)

screen_width = root.winfo_screenwidth() // 2 - 300 
screen_height = root.winfo_screenheight() // 2 - 300 
root.geometry('800x800+{}+{}'.format(screen_width, screen_height))
root.title("Главное окно")

root.mainloop()

json_string = """
{
    "data": {
        "адрес": "Спб, Сокольников 37",
        "фетиши": [
            {
                "черные": "никак",
                "тентакли": "средний",
                "ноги": "слабый",
                "худые": "сильный",
                "ЯОЙ": "средний"
            }
        ]
    }
}
"""


"""with conn.cursor() as cursor:
    sql = """""" UPDATE users
                SET personal_data = %s
                WHERE name = %s""""""
    try:
        # execute the UPDATE  statement
        cursor.execute(sql, (json_string, 'Васильева Алиса'))
        # get the number of updated rows
        conn.commit()
        # Close communication with the PostgreSQL database
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
"""