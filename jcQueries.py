import psycopg2
import datetime
from jcUserClass import User
from psycopg2 import sql


class DataBase:
    def __init__(self):
        self.name = 'db'
        self.user = 'postgres'
        self.password = 'Peony5155'
        self.host = 'localhost'

    def get_all_users(self):
        """
        Возвращает список всех объектов User из таблицы users
        """
        conn = psycopg2.connect(
            dbname=self.name, user=self.user, password=self.password, host=self.host)
        records = []
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM users')
            records = cursor.fetchall()
        conn.close()
        users = []
        if len(records) > 0:
            for rec in records:
                user = User(rec)
                users.append(user)
            return users
        else:
            return None

    def get_all_students(self):
        conn = psycopg2.connect(
            dbname=self.name, user=self.user, password=self.password, host=self.host)
        records = []
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM users WHERE type = %s ORDER BY name',
                           ('студент', ))
            records = cursor.fetchall()
        conn.close()
        users = []
        if len(records) > 0:
            for rec in records:
                user = User(rec)
                users.append(user)
            return users
        else:
            return None

    def get_consultants(self):
        conn = psycopg2.connect(
            dbname=self.name, user=self.user, password=self.password, host=self.host)
        records = []
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM users WHERE competence = %s ORDER BY name',
                           ('консультант', ))
            records = cursor.fetchall()
        conn.close()
        users = []
        if len(records) > 0:
            for rec in records:
                user = User(rec)
                users.append(user)
            return users
        else:
            return None

    def get_dispatchers(self):
        conn = psycopg2.connect(
            dbname=self.name, user=self.user, password=self.password, host=self.host)
        records = []
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM users WHERE competence = %s ORDER BY name',
                           ('диспетчер', ))
            records = cursor.fetchall()
        conn.close()
        users = []
        if len(records) > 0:
            for rec in records:
                user = User(rec)
                users.append(user)
            return users
        else:
            return None

    def insert_users(self, users):
        """
        Принимает список объектов User
        Добавляет их в таблицу users
        """
        conn = psycopg2.connect(
            dbname=self.name, user=self.user, password=self.password, host=self.host)
        try:
            conn.autocommit = True
            with conn.cursor() as cursor:
                values = []
                for u in users:
                    values.append(
                        (u.name, u.type, u.competence, u.login, u.password))
                insert = sql.SQL('INSERT INTO users(name, type, competence, login, password) VALUES {}').format(
                    sql.SQL(',').join(map(sql.Literal, values))
                )
                cursor.execute(insert)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return error
        finally:
            conn.close()

    def get_user_by_login(self, log):
        conn = psycopg2.connect(
            dbname=self.name, user=self.user, password=self.password, host=self.host)
        with conn.cursor() as cursor:
            conn.autocommit = True
            cursor.execute('SELECT * FROM users WHERE login = %s', (log, ))
            records = cursor.fetchall()
        conn.close()
        if len(records) > 0:
            user = User(records[0])
            return user
        else:
            return None

    def get_user_by_id(self, id):
        conn = psycopg2.connect(
            dbname=self.name, user=self.user, password=self.password, host=self.host)
        with conn.cursor() as cursor:
            conn.autocommit = True
            cursor.execute('SELECT * FROM users WHERE user_id = %s', (id, ))
            records = cursor.fetchall()
        conn.close()
        if len(records) > 0:
            user = User(records[0])
            return user
        else:
            return None

    def delete_user_by_id(self, id):
        if self.get_user_by_id(id) == None:
            return None
        conn = psycopg2.connect(
            dbname=self.name, user=self.user, password=self.password, host=self.host)
        with conn.cursor() as cursor:
            conn.autocommit = True
            cursor.execute('DELETE FROM users WHERE user_id = %s', (id, ))
        conn.close()
        return id

    def update_user_by_id(self, user):
        if self.get_user_by_id(user.id) == None:
            return None
        user_id = user.id
        conn = psycopg2.connect(
            dbname=self.name, user=self.user, password=self.password, host=self.host)
        with conn.cursor() as cursor:
            sql = """UPDATE users
                        SET name = %s,
                        type = %s,
                        competence = %s,
                        login =  %s,
                        password =  %s,
                        personal_data =  %s,
                        points = %s
                        WHERE user_id = %s"""
            try:
                # execute the UPDATE  statement
                cursor.execute(sql, (user.name, user.type, user.competence, user.login,
                                     user.password, user.personal_data, user.points, user_id))
                # get the number of updated rows
                conn.commit()
                # Close communication with the PostgreSQL database
                cursor.close()
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)

    def insert_cases(self, cases, disp_id, suppl_id):
        conn = psycopg2.connect(
            dbname=self.name, user=self.user, password=self.password, host=self.host)
        try:
            conn.autocommit = True
            with conn.cursor() as cursor:
                values = []
                for c in cases:
                    now = datetime.datetime.now()
                    values.append(
                        (c.category, c.title, c.description, None, None, "ожидает назначения ответственных",
                            suppl_id, disp_id, str(now)))
                insert = sql.SQL('INSERT INTO cases(category, title, description, s_id, t_id, status, supplicant_id, dispatcher_id, last_update) VALUES {}').format(
                    sql.SQL(',').join(map(sql.Literal, values))
                )
                cursor.execute(insert)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return error
        finally:
            conn.close()
