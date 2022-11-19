from CTime import CTime
import random
import datetime


class CUser:
    def __init__(self):
        # key = date, watts = value
        self.power_consumption = {}
        self.ctime = CTime()

    # add today's consumption
    def add_consumption(self):
        pass

    def get_consumption(self, period=None):
        if period is None:
            return self.power_consumption

        start_date, end_date = self.ctime.get_date(period)

        d = dict()
        delta = datetime.timedelta(days=1)

        while start_date <= end_date:
            watts = self.power_consumption.get(start_date)
            if watts is None:
                continue
            d.update({start_date: watts})
            start_date += delta
        return d

        # generates data from a user to show how our application works

    def generate_data(self):
        start_date = datetime.date(2016, 1, 1)
        end_date = datetime.date.today()
        delta = datetime.timedelta(days=1)

        while start_date <= end_date:
            random_wt = random.uniform(0.01, 0.02)
            self.power_consumption.update({start_date: random_wt})
            start_date += delta
