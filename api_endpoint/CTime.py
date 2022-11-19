import datetime


class CTime:
    def __init__(self):
        self.base = datetime.date.today()

    def get_date(self, period):
        """
        calculates days in given period of time
        :param period: string literal year / month / week / day
        :return: marginal values -> tuple (date, date)
        """
        if period == 'day':
            start_date, end_date = self.__day()

        elif period == 'week':
            start_date, end_date = self.__week()

        elif period == 'month':
            start_date, end_date = self.__month()

        elif period == 'year':
            start_date, end_date = self.__year()
        else:
            return None
        return start_date, end_date

    def __day(self):
        """
        calcultes current day
        :return:  marginal values -> tuple (date, date)
        """
        dates = [self.base - datetime.timedelta(days=x) for x in range(1)]
        return dates[-1], dates[0]

    def __week(self):
        """
        calculates week length of days
        :return: marginal values -> tuple (date, date)
        """
        dates = [self.base - datetime.timedelta(days=x) for x in range(7)]
        return dates[-1], dates[0]

    def __month(self):
        """
        calculates month lenght of days
        :return: marginal values -> tuple (date, date)
        """
        dates = [self.base - datetime.timedelta(days=x) for x in range(30)]
        return dates[-1], dates[0]

    def __year(self):
        dates = [self.base - datetime.timedelta(days=x) for x in range(365)]
        return dates[-1], dates[0]
