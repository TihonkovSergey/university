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
        """
        Принимает список объектов User
        Добавляет их в таблицу users 
        """
        conn = psycopg2.connect(dbname=self.name, user=self.user, password=self.password, host=self.host)
        try:
            conn.autocommit = True
            with conn.cursor() as cursor:
                values = []
                for u in users:
                    values.append((u.name, u.type, u.competence, u.login, u.password))
                insert = sql.SQL('INSERT INTO users(name, type, competence, login, password) VALUES {}').format(
                    sql.SQL(',').join(map(sql.Literal, values))
                )
                cursor.execute(insert)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return error
        finally:
            conn.close()
