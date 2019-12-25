import psycopg2
import datetime
from jcUserClass import User
from psycopg2 import sql
from jcSupplicantClass import Supplicant
from jcCaseClass import Case

from db_config import DB


class SupplicantQuery:
    def __init__(self):
        db = DB()
        self.name = db.name
        self.user = db.user
        self.password = db.password
        self.host = db.host

    def insert_supplicant(self, supplicant):
        conn = psycopg2.connect(
            dbname=self.name, user=self.user, password=self.password, host=self.host)
        try:
            conn.autocommit = True
            with conn.cursor() as cursor:
                values = []
                values.append(
                    (supplicant.name, supplicant.telephone_number))
                insert = sql.SQL('INSERT INTO supplicants(name, telephone_number) VALUES {} RETURNING supplicant_id').format(
                    sql.SQL(',').join(map(sql.Literal, values))
                )
                cursor.execute(insert)
                id_of_new_row = cursor.fetchone()[0]
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return error
        finally:
            conn.close()
            return id_of_new_row

    def get_supplicant_by_id(self, id):
        conn = psycopg2.connect(
            dbname=self.name, user=self.user, password=self.password, host=self.host)
        with conn.cursor() as cursor:
            conn.autocommit = True
            cursor.execute(
                'SELECT * FROM supplicants WHERE supplicant_id = %s', (id, ))
            records = cursor.fetchall()
        conn.close()
        if len(records) > 0:
            supplicant = Supplicant(records[0])
            return supplicant
        else:
            return None

    def delete_supplicant_by_id(self, id):
        if self.get_supplicant_by_id(id) == None:
            return None
        conn = psycopg2.connect(
            dbname=self.name, user=self.user, password=self.password, host=self.host)
        with conn.cursor() as cursor:
            conn.autocommit = True
            cursor.execute(
                'DELETE FROM supplicants WHERE supplicant_id = %s', (id, ))
        conn.close()
        return id
