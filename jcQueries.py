import psycopg2
import datetime
from jcUserClass import User
from psycopg2 import sql
from jcSupplicantClass import Supplicant
from jcCaseClass import Case

from usersQueries import UsersQuery
from pointsQueries import PointsQuery
from caseQueries import CaseQuery
from supplicantQueries import SupplicantQuery


class DataBase:
    def __init__(self):
        self.name = 'db'
        self.user = 'postgres'
        self.password = 'Peony5155'
        self.host = 'localhost'

    def insert_users(self, users):
        q = UsersQuery()
        return q.insert_users(users)

    def get_all_users(self):
        q = UsersQuery()
        return q.get_all_users()

    def get_user_by_login(self, log):
        q = UsersQuery()
        return q.get_user_by_login(log)

    def get_user_by_id(self, id):
        q = UsersQuery()
        return q.get_user_by_id(id)

    def delete_user_by_id(self, id):
        q = UsersQuery()
        return q.delete_user_by_id(id)

    def update_user_by_id(self, user):
        q = UsersQuery()
        return q.update_user_by_id(user)

    def get_all_students(self):
        q = UsersQuery()
        return q.get_all_students()

    def get_consultants(self):
        q = UsersQuery()
        return q.get_consultants()

    def get_dispatchers(self):
        q = UsersQuery()
        return q.get_dispatchers()

    def get_students_order_by_points(self):
        q = PointsQuery()
        return q.get_students_order_by_points()

    def get_dispatchers_order_by_points(self):
        q = PointsQuery()
        return q.get_dispatchers_order_by_points()

    def get_сonsultants_order_by_points(self):
        q = PointsQuery()
        return q.get_сonsultants_order_by_points()

    def insert_cases(self, cases, disp_id, suppl_id):
        q = CaseQuery()
        return q.insert_cases(cases, disp_id, suppl_id)

    def get_case_by_id(self, id):
        q = CaseQuery()
        return q.get_case_by_id(id)

    def get_cases_by_student_id(self, student_id):
        q = CaseQuery()
        return q.get_cases_by_student_id(student_id)

    def get_cases_by_teacher_id(self, teacher_id):
        q = CaseQuery()
        return q.get_cases_by_teacher_id(teacher_id)

    def insert_supplicant(self, supplicants):
        q = SupplicantQuery()
        return q.insert_supplicant(supplicants)

    def get_supplicant_by_id(self, id):
        q = SupplicantQuery()
        return q.get_supplicant_by_id(id)

    def delete_supplicant_by_id(self, id):
        q = SupplicantQuery()
        return q.delete_supplicant_by_id(id)
