import json


class Duty:
    def __init__(self, duty):
        self.duty_id = str(duty[0])
        self.s_id = str(duty[1])
        self.date = str(duty[2])
        self.status = str(duty[3])

    def __str__(self):
        return (self.duty_id + " " +
                self.s_id + " " +
                self.date + " " +
                self.status)

    def __print__(self):
        print(str(self))
