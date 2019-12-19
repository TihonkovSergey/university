import psycopg2
from jcUserClass import User
from psycopg2 import sql

DB_NAME = 'postgres'
DB_USER = 'postgres'
DB_PASSWORD = 'postgres'
DB_HOST = 'localhost'

class DataBase:
    def __init__(self):
        self.name ='postgres'
        self.user = 'postgres'
        self.password = 'postgres'
        self.host = 'localhost'

    def get_all_users(self):
        """
        Возвращает список всех объектов User из таблицы users
        """
        conn = psycopg2.connect(dbname=self.name, user=self.user, password=self.password, host=self.host)
        records = []
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM users')
            records = cursor.fetchall()
        conn.close()
        users = []
        for rec in records:
            user = User(rec)
            users.append(user)
        return users

    def insert_users(self, users):
        conn = psycopg2.connect(dbname=self.name, user=self.user, password=self.password, host=self.host)
        try:
            with conn.cursor() as cursor:
                values = []
                for u in users:
                    values.append((u.name, u.type, u.competence, u.login, u.password))
                insert = sql.SQL('INSERT INTO users (name, type, competence, login, password) VALUES {}').format(
                    sql.SQL(',').join(map(sql.Literal, values))
                )
                cursor.execute(insert)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            conn.close()
    
    def insert_user_list(self, user_list):
        sql = "INSERT INTO users(name, type, competence, login, password) VALUES(%s)"
        conn = None
        try:
            # connect to the PostgreSQL database
            conn = psycopg2.connect(dbname=self.name, user=self.user, password=self.password, host=self.host)
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.executemany(sql,user_list)
            # commit the changes to the database
            conn.commit()
            # close communication with the database
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

db = DataBase()
user1 = User(('some_id', 'Сидорова Надежда Петровна', 'преподаватель', 'административное дело', 'st000000', '1234', '{}'))
user2 = User(('some_id', 'Печалина Людмила Николаевна', 'преподаватель', 'административное дело', 'st000001', '1234', '{}'))

list_users = [(u'Сидорова Надежда Петровна', u'преподаватель', u'административное дело', u'st000000', u'1234',),]
#list_users.append(user1)
#list_users.append(user2)

db.insert_user_list(list_users)
users = db.get_all_users()
for u in users:
    print(u)