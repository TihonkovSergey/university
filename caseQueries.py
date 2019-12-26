import psycopg2
import datetime
from jcUserClass import User
from psycopg2 import sql

from jcCaseClass import Case

from db_config import DB


class CaseQuery:
    def __init__(self):
        db = DB()
        self.name = db.name
        self.user = db.user
        self.password = db.password
        self.host = db.host

    def insert_case(self, case):
        conn = psycopg2.connect(
            dbname=self.name, user=self.user, password=self.password, host=self.host)
        try:
            conn.autocommit = True
            with conn.cursor() as cursor:
                values = []
                now = datetime.datetime.now()
                values.append(
                    (case.category, case.title, case.description, None, None, "ожидает назначения ответственных",
                     case.supplicant_id, case.dispatcher_id, str(now)))
                insert = sql.SQL('INSERT INTO cases(category, title, description, s_id, t_id, status, supplicant_id, dispatcher_id, last_update) VALUES {} RETURNING case_id').format(
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

    def get_case_by_id(self, id):
        conn = psycopg2.connect(
            dbname=self.name, user=self.user, password=self.password, host=self.host)
        with conn.cursor() as cursor:
            conn.autocommit = True
            cursor.execute('SELECT * FROM cases WHERE case_id = %s', (id, ))
            records = cursor.fetchall()
        conn.close()
        if len(records) > 0:
            case = Case(records[0])
            return case
        else:
            return None

    def get_all_cases(self):
        conn = psycopg2.connect(
            dbname=self.name, user=self.user, password=self.password, host=self.host)
        records = []
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM cases')
            records = cursor.fetchall()
        conn.close()
        cases = []
        if len(records) > 0:
            for rec in records:
                case = Case(rec)
                cases.append(case)
            return cases
        else:
            return None

    def delete_case_by_case_id(self, case_id):
        if self.get_case_by_id(case_id) == None:
            return None
        conn = psycopg2.connect(
            dbname=self.name, user=self.user, password=self.password, host=self.host)
        with conn.cursor() as cursor:
            conn.autocommit = True
            cursor.execute('DELETE FROM cases WHERE case_id = %s', (case_id, ))
        conn.close()
        return case_id

    def update_case_by_id(self, case):
        if self.get_case_by_id(case.case_id) == None:
            return None
        case_id = case.case_id
        conn = psycopg2.connect(
            dbname=self.name, user=self.user, password=self.password, host=self.host)
        with conn.cursor() as cursor:
            now = datetime.datetime.now()
            sql = """UPDATE cases
                        SET category = %s,
                        title = %s,
                        description = %s,
                        s_id =  %s,
                        t_id =  %s,
                        status =  %s,
                        supplicant_id = %s,
                        dispatcher_id = %s,
                        last_update = %s
                        WHERE case_id = %s"""
            try:
                # execute the UPDATE  statement
                cursor.execute(sql, (case.category, case.title, case.description, case.s_id,
                                     case.t_id, case.status, case.supplicant_id, case.dispatcher_id, str(
                                         now),
                                     case_id))
                # get the number of updated rows
                conn.commit()
                # Close communication with the PostgreSQL database
                cursor.close()
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)

    def get_cases_which_need_student_editing(self, student_id):
        conn = psycopg2.connect(
            dbname=self.name, user=self.user, password=self.password, host=self.host)
        records = []
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM cases WHERE (status = %s OR status = %s) AND (s_id = %s) ORDER BY title',
                           ('ожидаются правки плана консультации', 'ожидаются правки резолюции', student_id))
            records = cursor.fetchall()
        conn.close()
        cases = []
        if len(records) > 0:
            for rec in records:
                case = Case(rec)
                cases.append(case)
            return cases
        else:
            return None

    def get_cases_which_need_teacher_editing(self, teacher_id):
        conn = psycopg2.connect(
            dbname=self.name, user=self.user, password=self.password, host=self.host)
        records = []
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM cases WHERE (status = %s OR status = %s) AND (t_id = %s) ORDER BY title',
                           ('ожидается проверка правок плана консультации', 'ожидается проверка правок резолюции', teacher_id))
            records = cursor.fetchall()
        conn.close()
        cases = []
        if len(records) > 0:
            for rec in records:
                case = Case(rec)
                cases.append(case)
            return cases
        else:
            return None

    def get_student_completed_cases(self, student_id):
        conn = psycopg2.connect(
            dbname=self.name, user=self.user, password=self.password, host=self.host)
        records = []
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM cases WHERE (status = %s) AND (s_id = %s) ORDER BY title',
                           ('завершено', student_id))
            records = cursor.fetchall()
        conn.close()
        cases = []
        if len(records) > 0:
            for rec in records:
                case = Case(rec)
                cases.append(case)
            return cases
        else:
            return None

    def get_teacher_completed_cases(self, teacher_id):
        conn = psycopg2.connect(
            dbname=self.name, user=self.user, password=self.password, host=self.host)
        records = []
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM cases WHERE (status = %s) AND (t_id = %s) ORDER BY title',
                           ('завершено', teacher_id))
            records = cursor.fetchall()
        conn.close()
        cases = []
        if len(records) > 0:
            for rec in records:
                case = Case(rec)
                cases.append(case)
            return cases
        else:
            return None

    def get_cases_by_student_id(self, student_id):
        conn = psycopg2.connect(
            dbname=self.name, user=self.user, password=self.password, host=self.host)
        records = []
        with conn.cursor() as cursor:
            conn.autocommit = True
            cursor.execute(
                'SELECT * FROM cases WHERE s_id = %s', (student_id, ))
            records = cursor.fetchall()
        conn.close()
        cases = []
        if len(records) > 0:
            for rec in records:
                cs = Case(rec)
                cases.append(cs)
            return cases
        else:
            return None

    def get_cases_by_teacher_id(self, teacher_id):
        conn = psycopg2.connect(
            dbname=self.name, user=self.user, password=self.password, host=self.host)
        records = []
        with conn.cursor() as cursor:
            conn.autocommit = True
            cursor.execute(
                'SELECT * FROM cases WHERE t_id = %s', (teacher_id, ))
            records = cursor.fetchall()
        conn.close()
        cases = []
        if len(records) > 0:
            for rec in records:
                cs = Case(rec)
                cases.append(cs)
            return cases
        else:
            return None

    def get_all_completed_cases(self):
        conn = psycopg2.connect(
            dbname=self.name, user=self.user, password=self.password, host=self.host)
        records = []
        with conn.cursor() as cursor:
            cursor.execute(
                'SELECT * FROM cases WHERE status = %s', ('завершено', ))
            records = cursor.fetchall()
        conn.close()
        cases = []
        if len(records) > 0:
            for rec in records:
                case = Case(rec)
                cases.append(case)
            return cases
        else:
            return None

    def get_all_cases_waiting_for_appointment(self):
        conn = psycopg2.connect(
            dbname=self.name, user=self.user, password=self.password, host=self.host)
        records = []
        with conn.cursor() as cursor:
            cursor.execute(
                'SELECT * FROM cases WHERE status = %s', ('ожидает назначения ответственных', ))
            records = cursor.fetchall()
        conn.close()
        cases = []
        if len(records) > 0:
            for rec in records:
                case = Case(rec)
                cases.append(case)
            return cases
        else:
            return None
