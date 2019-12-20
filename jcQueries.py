import psycopg2
import datetime
from jcUserClass import User
from psycopg2 import sql
from jcSupplicantClass import Supplicant
from jcCaseClass import Case


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
    """ """

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

    def get_cases_which_need_student_editing(self, student_id):  # сережа долб
        conn = psycopg2.connect(
            dbname=self.name, user=self.user, password=self.password, host=self.host)
        records = []
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM cases WHERE status = %s OR status = %s ORDER BY title',
                           ('ожидаются правки плана консультации', 'ожидаются правки резолюции'))
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

    def get_cases_which_need_teacher_editing(self, teacher_id):  # сережа долб
        conn = psycopg2.connect(
            dbname=self.name, user=self.user, password=self.password, host=self.host)
        records = []
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM cases WHERE status = %s OR status = %s ORDER BY title',
                           ('ожидается проверка правок плана консультации', 'ожидается проверка правок резолюции'))
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

    def insert_supplicant(self, supplicants):
        conn = psycopg2.connect(
            dbname=self.name, user=self.user, password=self.password, host=self.host)
        try:
            conn.autocommit = True
            with conn.cursor() as cursor:
                values = []
                for s in supplicants:
                    values.append(
                        (s.name, s.telephone_number))
                insert = sql.SQL('INSERT INTO supplicants(name, telephone_number) VALUES {}').format(
                    sql.SQL(',').join(map(sql.Literal, values))
                )
                cursor.execute(insert)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return error
        finally:
            conn.close()

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
