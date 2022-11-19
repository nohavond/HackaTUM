import datetime
import json

from CTime import CTime


class CStock:
    def __init__(self):
        self.power_prices = dict()
        self.ctime = CTime()
        self.__get_data()

    # for the future there can be used site https://tradingeconomics.com/germany/electricity-price
    # they also do provide simple API to get their data, but we do not have permission to access them
    def __get_data(self):
        with open('stock_dummy.json') as json_file:
            power_prices = json.load(json_file)

        for key, val in power_prices.items():
            date_obj = datetime.datetime.strptime(key, '%Y-%m-%d').date()
            self.power_prices.update({date_obj: val})

    # show current MWh prices in chosen period
    def get_prices(self, period):
        start_date, end_date = self.ctime.get_date(period)
        d = dict()
        delta = datetime.timedelta(days=1)
        while start_date <= end_date:
            price = self.power_prices.get(start_date)
            d.update({start_date: price})
            start_date += delta
        return d
