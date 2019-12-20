import json


class User:
    def __init__(self, user):
        self.id = str(user[0])
        self.name = str(user[1])
        self.type = str(user[2])
        self.competence = str(user[3])
        self.login = str(user[4])
        self.password = str(user[5])
        self.personal_data = str(user[6])

    def __str__(self):
        return (self.id + " " +
                self.name + " " +
                self.type + " " +
                self.competence + " " +
                self.login + " " +
                self.password + " " +
                self.personal_data)

    def __print__(self):
        print(str(self))

    def __eq__(self, other):
        if (not other):
            return False
        return (self.id == other.id and
                self.name == other.name and
                self.type == other.type and
                self.competence == other.competence and
                self.login == other.login and
                self.password == other.password and
                self.personal_data == other.personal_data)
