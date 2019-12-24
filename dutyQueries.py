import psycopg2
import datetime
from jcUserClass import User
from psycopg2 import sql

from jcCaseClass import Case
from jcDocumentsClass import Document
from jcDutyClass import Duty

from db_config import DB


class DutyQuery:
    def __init__(self):
        db = DB()
        self.name = db.name
        self.user = db.user
        self.password = db.password
        self.host = db.host

    def insert_duty(self, duty):
        conn = psycopg2.connect(
            dbname=self.name, user=self.user, password=self.password, host=self.host)
        try:
            conn.autocommit = True
            with conn.cursor() as cursor:
                values = []
                values.append(
                    (duty.duty_id, duty.s_id, duty.date, "дежурство ожидается"))
                insert = sql.SQL('INSERT INTO duty_feed(duty_id, s_id, date, status) VALUES {}').format(
                    sql.SQL(',').join(map(sql.Literal, values))
                )
                cursor.execute(insert)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return error
        finally:
            conn.close()

    def get_duties_by_s_id(self, student_id):
        conn = psycopg2.connect(
            dbname=self.name, user=self.user, password=self.password, host=self.host)
        records = []
        with conn.cursor() as cursor:
            conn.autocommit = True
            cursor.execute(
                'SELECT * FROM duty_feed WHERE s_id = %s', (student_id, ))
            records = cursor.fetchall()
        conn.close()
        duties = []
        if len(records) > 0:
            for rec in records:
                duty = Duty(rec)
                duties.append(duty)
            return duties
        else:
            return None

    def get_duty_by_id(self, duty_id):
        conn = psycopg2.connect(
            dbname=self.name, user=self.user, password=self.password, host=self.host)
        with conn.cursor() as cursor:
            conn.autocommit = True
            cursor.execute(
                'SELECT * FROM duty_feed WHERE duty_id = %s', (duty_id, ))
            records = cursor.fetchall()
        conn.close()
        if len(records) > 0:
            duty = Duty(records[0])
            return duty
        else:
            return None

    def delete_duty_by_id(self, duty_id):
        if self.get_duty_by_id(duty_id) == None:
            return None
        conn = psycopg2.connect(
            dbname=self.name, user=self.user, password=self.password, host=self.host)
        with conn.cursor() as cursor:
            conn.autocommit = True
            cursor.execute(
                'DELETE FROM duty_feed WHERE duty_id = %s', (duty_id, ))
        conn.close()
        return duty_id
