import psycopg2
from jcUserClass import User
from jcQueries import DataBase
from psycopg2 import sql
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import json
from jcDocumentsClass import Document
from tkcalendar import DateEntry
import datetime

db = DataBase()
now = datetime.datetime.now()
print(str(now).split()[0])

data = {
    "users": [
        {
            "id": "id",
            "name": "Сергеев Сергей Консультантов",
            "type": "студент",
            "competence": "консультант",
            "login": "st111111",
            "password": "0000",
                        "personal_data": "",
                        "points": "0.0"
        },
        {
            "id": "id",
            "name": "Первак Андрей Андреевич",
            "type": "преподаватель",
            "competence": "граждансое право",
            "login": "st124141",
            "password": "0000",
                        "personal_data": "",
                        "points": "0.0"
        },
        {
            "id": "id",
            "name": "Жуткова Алена Васильевна",
            "type": "преподаватель",
            "competence": "трудовое право",
            "login": "st123532",
            "password": "0000",
                        "personal_data": "",
                        "points": "0.0"
        },
        {
            "id": "id",
            "name": "Мятникова Ирга Федоровна",
            "type": "преподаватель",
            "competence": "трудовое право",
            "login": "st121531",
            "password": "0000",
                        "personal_data": "",
                        "points": "0.0"
        },
        {
            "id": "id",
            "name": "Иванов Иван Петрович",
            "type": "студент",
            "competence": "диспетчер",
            "login": "st654321",
            "password": "0000",
                        "personal_data": "",
                        "points": "0.0"
        },
        {
            "id": "id",
            "name": "Левченко Авдотья Николаевна",
            "type": "преподаватель",
            "competence": "административное право",
            "login": "st122331",
            "password": "0000",
                        "personal_data": "",
                        "points": "0.0"
        },
        {
            "id": "id",
            "name": "Петров Борис Владиславович",
            "type": "студент",
            "competence": "консультант",
            "login": "st125531",
            "password": "0000",
                        "personal_data": "",
                        "points": "0.0"
        },
        {
            "id": "id",
            "name": "Петрова Ульяна Сергеевна",
            "type": "студент",
            "competence": "диспетчер",
            "login": "st065531",
            "password": "0000",
                        "personal_data": "",
                        "points": "0.0"
        },
        {
            "id": "id",
            "name": "Пронко Мария Владиславовна",
            "type": "студент",
            "competence": "консультант",
            "login": "st124431",
            "password": "0000",
                        "personal_data": "",
                        "points": "0.0"
        },
        {
            "id": "id",
            "name": "Рожкова Анастасия Марковна",
            "type": "студент",
            "competence": "диспетчер",
            "login": "st125534",
            "password": "0000",
                        "personal_data": "",
                        "points": "0.0"
        },
        {
            "id": "id",
            "name": "Неверова Патриция Аркадьевна",
            "type": "преподаватель",
            "competence": "жилищное право",
            "login": "st131531",
            "password": "0000",
                        "personal_data": "",
                        "points": "0.0"
        },
        {
            "id": "id",
            "name": "Чукчина Эльвира Маратовна",
            "type": "преподаватель",
            "competence": "гражданское право",
            "login": "st125555",
            "password": "0000",
                        "personal_data": "",
                        "points": "0.0"
        },
        {
            "id": "id",
            "name": "Верхеев Игорь Игоревич",
            "type": "преподаватель",
            "competence": "административное право",
            "login": "st385627",
            "password": "0000",
                        "personal_data": "",
                        "points": "0.0"
        },
        {
            "id": "id",
            "name": "Купцова Ольга Михайловна",
            "type": "тьютор",
            "competence": "юридическая клиника",
            "login": "tutor",
            "password": "0000",
                        "personal_data": "",
                        "points": "0.0"
        },
        {
            "id": "id",
            "name": "Иванов Денис Юрьевич",
            "type": "админ",
            "competence": "юридическая клиника",
            "login": "admin",
            "password": "1111",
                        "personal_data": "",
                        "points": "0.0"
        },
        {
            "id": "id",
            "name": "Ионова Алина Евшеньевна",
            "type": "студент",
            "competence": "консультант",
            "login": "st222222",
            "password": "2222",
                        "personal_data": "",
                        "points": "0.0"
        },
        {
            "id": "id",
            "name": "Романов Борис Павлович",
            "type": "студент",
            "competence": "диспетчер",
            "login": "st333333",
            "password": "3333",
                        "personal_data": "",
                        "points": "0.0"
        }
    ]
}

"""file_name = fd.askopenfilename(filetypes=(("Json FILES", "*.json"),
                                                        ("All files", "*.*") ))
if not file_name:
	mb.showerror("Ошибка", "Вы не выбрали файл!")
file_path_list = file_name.split("/")
print(file_path_list[-1])
# doc = Document((file_name,))
"""
"""
file_name = fd.askopenfilename()


with open(file_name, "w") as write_file:
    json.dump(data, write_file)

# file_name = "D:/homeworks/university_databases/add_users.json"

file_name = fd.askopenfilename()
print(file_name)
f = open(file_name)

new_data = json.load(f)

f.close()

for data in new_data["users"]:
		user = User((data["id"], data["name"], data["type"], data["competence"],
		            data["login"], data["password"], data["personal_data"], data["points"]))
		print(user.name)
# print(new_data["users"][0])
"""
"""
user = User(("id", "Главный Админ Админов", "админ",
            "админ", "admin", "0000", "", "0.0"))
db.insert_users([user])

users = db.get_all_users()
for u in users:
    print(u)"""

"""event = db.get_points_event_by_id("1")
print(event)
"""

"""
user = db.get_user_by_id(1)
user.name+= " Алексеевич"
db.update_user_by_id(user)
user = db.get_user_by_id(1)
print(user)
"""
