import login_window
import teacher_window
import my_cases_window
import my_students_window
import my_profile_window
import profile_window
import case_window

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