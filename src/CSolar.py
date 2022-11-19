import datetime


class CTime:
    def __init__(self):
        self.base = datetime.datetime.today()

    def day(self):
        return self.base

    def week(self):
        return [self.base - datetime.timedelta(days=x) for x in range(7)]

    def month(self):
        return [self.base - datetime.timedelta(days=x) for x in range(30)]

    def year(self):
        return [self.base - datetime.timedelta(days=x) for x in range(365)]


class CSolar:
    def __init__(self, user):
        self.user = user
        self.ctime = CTime()

    # compare energy consumption with current
    # energy prices in germany and show the user
    # how much money can he save
    def show_savings(self, period):
        if period == 'week':
            dates = self.ctime.week()

        elif period == 'month':
            dates = self.ctime.month()

        else:
            dates = self.ctime.year()

    # show current MWh prices in chosen period
    def show_prices(self, period):
        pass

    # generates data from a user to show how our application works
    def generate_data(self):
        pass
