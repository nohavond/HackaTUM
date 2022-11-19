from CTime import CTime
import random
import datetime


class CUser:
    def __init__(self, zip_code=None):
        # key = date, watts = value
        self.power_consumption = {}
        self.ctime = CTime()
        self.zip = zip_code

    # add today's consumption
    def add_consumption(self):
        pass

    def add_address(self, zip_code):
        pass

    """
    Shows how many days is user active in the app
    """

    def active(self):
        return len(self.power_consumption)

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

    def generate_data(self):
        start_date = datetime.date(2016, 1, 1)
        end_date = datetime.date.today()
        delta = datetime.timedelta(days=1)

        while start_date <= end_date:
            random_wt = random.uniform(800, 3000)
            self.power_consumption.update({start_date: random_wt})
            start_date += delta
