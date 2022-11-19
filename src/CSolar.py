from CTime import CTime
from CUser import CUser
import pandas as pd
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

        dates = user.get_consumption(period)
        result = 0
        print('You could have saved: ' + str(result) + '€')

    def __calcualte_savings(self, period):
        pass

    # calculate generated energy based on number of hours of daylight
    # for simplification we expect sun light to be const value of 4 hours
    def __generated_energy(self, sunlight=4, panel_power=400):
        return panel_power * sunlight
