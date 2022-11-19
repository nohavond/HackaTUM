from CTime import CTime


class CSolar:
    def __init__(self):
        self.ctime = CTime()

    # compare energy consumption with current
    # energy prices in germany and show the user
    # how much money can he save
    def show_savings(self, user, period):
        if period == 'week':
            dates = self.ctime.week()

        elif period == 'month':
            dates = self.ctime.month()

        else:
            dates = self.ctime.year()

    # show current MWh prices in chosen period
    def show_prices(self, period):
        pass

