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
            self.power_prices = json.load(json_file)

        # show current MWh prices in chosen period

    def show_prices(self, period):
        dates = self.ctime.get_date(period)

