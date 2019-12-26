import psycopg2
import datetime
from jcUserClass import User
from psycopg2 import sql
from jcSupplicantClass import Supplicant
from jcCaseClass import Case
from jcPointsEventClass import PointsEvent
from jcDocumentsClass import Document
from jcDutyClass import Duty

from usersQueries import UsersQuery
from pointsQueries import PointsQuery
from caseQueries import CaseQuery
from supplicantQueries import SupplicantQuery
from documentQueries import DocumentQuery
from dutyQueries import DutyQuery

from db_config import DB


class DataBase:
    def __init__(self):
        self.name = ""
        self.user = ""
        self.password = ""
        self.host = ""

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

    def get_teachers_by_competence(self, competence):
        q = UsersQuery()
        return q.get_teachers_by_competence(competence)

    """"""

    def insert_points_event(self, points_events):
        q = PointsQuery()
        return q.insert_points_event(points_events)

    def get_points_event_by_id(self, id):
        q = PointsQuery()
        return q.get_points_event_by_id(id)

    def get_points_event_by_s_id(self, student_id):
        q = PointsQuery()
        return q.get_points_event_by_s_id(student_id)

    def get_points_event_by_t_id(self, teacher_id):
        q = PointsQuery()
        return q.get_points_event_by_t_id(teacher_id)

    def get_students_order_by_points(self):
        q = PointsQuery()
        return q.get_students_order_by_points()

    def get_dispatchers_order_by_points(self):
        q = PointsQuery()
        return q.get_dispatchers_order_by_points()

    def get_сonsultants_order_by_points(self):
        q = PointsQuery()
        return q.get_сonsultants_order_by_points()

    """"""

    def insert_case(self, cases):
        q = CaseQuery()
        return q.insert_case(cases)

    def get_case_by_id(self, id):
        q = CaseQuery()
        return q.get_case_by_id(id)

    def get_all_cases(self):
        q = CaseQuery()
        return q.get_all_cases()

    def delete_case_by_case_id(self, case_id):
        q = CaseQuery()
        return q.delete_case_by_case_id(case_id)

    def update_case_by_id(self, case):
        q = CaseQuery()
        return q.update_case_by_id(case)

    def get_cases_which_need_student_editing(self, student_id):
        q = CaseQuery()
        return q.get_cases_which_need_student_editing(student_id)

    def get_cases_which_need_teacher_editing(self, teacher_id):
        q = CaseQuery()
        return q.get_cases_which_need_teacher_editing(teacher_id)

    def get_all_completed_cases(self):
        q = CaseQuery()
        return q.get_all_completed_cases()

    def get_all_cases_waiting_for_appointment(self):
        q = CaseQuery()
        return q.get_all_cases_waiting_for_appointment()

    def get_student_completed_cases(self, student_id):
        q = CaseQuery()
        return q.get_student_completed_cases(student_id)

    def get_teacher_completed_cases(self, teacher_id):
        q = CaseQuery()
        return q.get_teacher_completed_cases(teacher_id)

    def get_cases_by_student_id(self, student_id):
        q = CaseQuery()
        return q.get_cases_by_student_id(student_id)

    def get_cases_by_teacher_id(self, teacher_id):
        q = CaseQuery()
        return q.get_cases_by_teacher_id(teacher_id)

    """"""

    def insert_supplicant(self, supplicant):
        q = SupplicantQuery()
        return q.insert_supplicant(supplicant)

    def get_supplicant_by_id(self, id):
        q = SupplicantQuery()
        return q.get_supplicant_by_id(id)

    def delete_supplicant_by_id(self, id):
        q = SupplicantQuery()
        return q.delete_supplicant_by_id(id)

    """"""

    def insert_document(self, document):
        q = DocumentQuery()
        return q.insert_document(document)

    def get_document_by_id(self, document_id):
        q = DocumentQuery()
        return q.get_document_by_id(document_id)

    def get_documents_by_case_id(self, case_id):
        q = DocumentQuery()
        return q.get_documents_by_case_id(case_id)

    def delete_document_by_id(self, document_id):
        q = DocumentQuery()
        return q.delete_document_by_id(document_id)

    """"""

    def insert_duty(self, duty):
        q = DutyQuery()
        return q.insert_duty(duty)

    def get_duty_by_id(self, duty_id):
        q = DutyQuery()
        return q.get_duty_by_id(duty_id)

    def get_duties_by_s_id(self, student_id):
        q = DutyQuery()
        return q.get_duties_by_s_id(student_id)

    def delete_duty_by_id(self, duty_id):
        q = DutyQuery()
        return q.delete_duty_by_id(duty_id)

    def update_duty_by_id(self, duty):
        q = DutyQuery()
        return q.update_duty_by_id(duty)

    def get_prev_duties(self):
        q = DutyQuery()
        return q.get_prev_duties()

    def get_next_duties(self):
        q = DutyQuery()
        return q.get_next_duties()

    def get_prev_duties_for_particular_student(self, student_id):
        q = DutyQuery()
        return q.get_prev_duties_for_particular_student(student_id)

    def get_next_duties_for_particular_student(self, student_id):
        q = DutyQuery()
        return q.get_next_duties_for_particular_student(student_id)
