import json
import datetime
#from jcQueries import DataBase
from jcSupplicantClass import Supplicant


class Case:
    def __init__(self, case):
        self.case_id = str(case[0])
        self.category = str(case[1])
        self.title = str(case[2])
        self.description = str(case[3])
        self.s_id = str(case[4])
        self.t_id = str(case[5])
        self.status = str(case[6])
        self.supplicant_id = str(case[7])
        self.dispatcher_id = str(case[8])
        self.last_update = str(case[9])

    def __str__(self):
        return (self.case_id + " " +
                self.category + " " +
                self.title + " " +
                self.description + " " +
                self.s_id + " " +
                self.t_id + " " +
                self.status + " " +
                self.supplicant_id + " " +
                self.dispatcher_id + " " +
                self.last_update)

    def __print__(self):
        print(str(self))
