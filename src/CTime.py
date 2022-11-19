import datetime


class CTime:
    def __init__(self):
        self.base = datetime.date.today()

    def day(self):
        dates = [self.base - datetime.timedelta(days=x) for x in range(1)]
        return dates[-1], dates[0]

    def week(self):
        dates = [self.base - datetime.timedelta(days=x) for x in range(7)]
        return dates[-1], dates[0]

    def month(self):
        dates = [self.base - datetime.timedelta(days=x) for x in range(30)]
        return dates[-1], dates[0]

    def year(self):
        dates = [self.base - datetime.timedelta(days=x) for x in range(365)]
        return dates[-1], dates[0]

