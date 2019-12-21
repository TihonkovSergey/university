import psycopg2
import datetime

from psycopg2 import sql
from jcUserClass import User
from jcPointsEventClass import PointsEvent

from db_config import DB


class PointsQuery:
    def __init__(self):
        db = DB()
        self.name = db.name
        self.user = db.user
        self.password = db.password
        self.host = db.host

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

    def insert_points_event(self, points_events):
        conn = psycopg2.connect(
            dbname=self.name, user=self.user, password=self.password, host=self.host)
        try:
            conn.autocommit = True
            with conn.cursor() as cursor:
                values = []
                for p in points_events:
                    now = datetime.datetime.now()
                    values.append(
                        (p.points, p.s_id, p.t_id, p.reason, str(now)))
                insert = sql.SQL('INSERT INTO points_feed(points, s_id, t_id, reason, date_time) VALUES {}').format(
                    sql.SQL(',').join(map(sql.Literal, values))
                )
                cursor.execute(insert)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return error
        finally:
            conn.close()

    def get_points_event_by_id(self, id):
        conn = psycopg2.connect(
            dbname=self.name, user=self.user, password=self.password, host=self.host)
        with conn.cursor() as cursor:
            conn.autocommit = True
            cursor.execute(
                'SELECT * FROM points_feed WHERE event_id = %s', (id, ))
            records = cursor.fetchall()
        conn.close()
        if len(records) > 0:
            event = PointsEvent(records[0])
            return event
        else:
            return None

    def get_points_event_by_s_id(self, student_id):
        conn = psycopg2.connect(
            dbname=self.name, user=self.user, password=self.password, host=self.host)
        records = []
        with conn.cursor() as cursor:
            conn.autocommit = True
            cursor.execute(
                'SELECT * FROM points_feed WHERE s_id = %s', (student_id, ))
            records = cursor.fetchall()
        conn.close()
        events = []
        if len(records) > 0:
            for rec in records:
                ev = PointsEvent(rec)
                events.append(ev)
            return events
        else:
            return None

    def get_points_event_by_t_id(self, teacher_id):
        conn = psycopg2.connect(
            dbname=self.name, user=self.user, password=self.password, host=self.host)
        records = []
        with conn.cursor() as cursor:
            conn.autocommit = True
            cursor.execute(
                'SELECT * FROM points_feed WHERE t_id = %s', (teacher_id, ))
            records = cursor.fetchall()
        conn.close()
        events = []
        if len(records) > 0:
            for rec in records:
                ev = PointsEvent(rec)
                events.append(ev)
            return events
        else:
            return None
