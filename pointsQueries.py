import psycopg2
import datetime
from jcUserClass import User
from psycopg2 import sql


class PointsQuery:
    def __init__(self):
        self.name = 'db'
        self.user = 'postgres'
        self.password = 'Peony5155'
        self.host = 'localhost'

    def get_students_order_by_points(self):
        conn = psycopg2.connect(
            dbname=self.name, user=self.user, password=self.password, host=self.host)
        records = []
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM users WHERE type = %s ORDER BY points',
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

    def get_dispatchers_order_by_points(self):
        conn = psycopg2.connect(
            dbname=self.name, user=self.user, password=self.password, host=self.host)
        records = []
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM users WHERE competence = %s ORDER BY points',
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

    def get_сonsultants_order_by_points(self):
        conn = psycopg2.connect(
            dbname=self.name, user=self.user, password=self.password, host=self.host)
        records = []
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM users WHERE competence = %s ORDER BY points',
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
