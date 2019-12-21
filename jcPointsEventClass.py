import datetime


class PointsEvent:
    def __init__(self, case):
        self.event_id = str(case[0])
        self.points = str(case[1])
        self.s_id = str(case[2])
        self.t_id = str(case[3])
        self.reason = str(case[4])
        self.date_time = str(case[5])

    def __str__(self):
        return (self.event_id + " " +
                self.points + " " +
                self.s_id + " " +
                self.t_id + " " +
                self.reason + " " +
                self.date_time)

    def __print__(self):
        print(str(self))
