import random

from CTime import CTime
from CUser import CUser
import datetime
from CStock import CStock


class CSolar:
    def __init__(self):
        self.ctime = CTime()
        self.stock = CStock()

    """
    compare energy consumption with current
    energy prices in germany and show the user
    how much money he can save, for each day we
    take into account current day price of energy
    """

    def show_savings(self, period, user=CUser()):
        if len(user.power_consumption) == 0:
            print('You could have saved: 0€')
            return

        result = self.__calculate_savings(period, user)
        print('You could have saved: ' + format(result, ',.2f') + '€')

    def __calculate_savings(self, period, user):
        start_date, end_date = self.ctime.get_date(period)
        price_data = self.stock.get_prices(period)
        user_data = user.get_consumption(period)

        delta = datetime.timedelta(days=1)

        normal_bill = 0
        eco_bill = 0
        while start_date <= end_date:
            user_consumption = user_data.get(start_date)
            price = price_data.get(start_date)
            could_be_generated = self.__generated_energy()

            normal_bill += (price * user_consumption)
            # consumption with solar panels
            eco_consumption = user_consumption - could_be_generated

            if eco_consumption > 0:
                eco_bill += (price * eco_consumption)
            start_date += delta

        return normal_bill - eco_bill

    # calculate generated energy based on number of hours of daylight
    # for simplification we expect sun light to be const value of 4 hours
    def __generated_energy(self, sunlight=4, panel_power=400):
        return panel_power * sunlight
