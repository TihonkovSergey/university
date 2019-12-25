import login_window
import teacher_window
import my_cases_window
import my_students_window
import my_profile_window
import profile_window
import case_window
import consultant_window
import add_points_window
import tutor_window
import my_duty_window
import dispatcher_window
import my_points_window
import admin_window
import my_teachers_window
import add_case_window
import add_cons_teach_window

def show_login(main_user):
    login_window.show_login(main_user)

def show_teacher(main_user):
    teacher_window.show_teacher(main_user)

def show_my_cases(main_user):
    my_cases_window.show_my_cases(main_user)

def show_my_students(main_user):
    my_students_window.show_my_students(main_user)

def show_my_profile(main_user):
    my_profile_window.show_my_profile(main_user)

def show_profile(main_user, user):
    profile_window.show_profile(main_user, user)

def show_case_window(main_user, case):
    case_window.show_case(main_user, case)

def show_consultant_window(main_user):
    consultant_window.show_consultant(main_user)

def show_add_points_window(main_user, user):
    add_points_window.show_add_points(main_user, user)

def show_tutor_window(main_user):
    tutor_window.show_tutor(main_user)

def show_my_duties(main_user):
    my_duty_window.show_my_duties(main_user)

def show_dispatcher_window(main_user):
    dispatcher_window.show_dispatcher(main_user)

def show_my_points_window(main_user):
    my_points_window.show_points(main_user)

def show_admin_window(main_user):
    admin_window.show_admin(main_user)

def show_my_teachers_window(main_user):
    my_teachers_window.show_my_teachers(main_user)

def show_add_case_window(main_user):
    add_case_window.add_case(main_user)

def show_add_cons_teach_window(main_user, case):
    add_cons_teach_window.add_cons_teach(main_user, case)