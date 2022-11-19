import datetime

from CStock import CStock
from CTime import CTime
from CUser import CUser


class CSolar:

    def __init__(self):
        self.ctime = CTime()
        self.stock = CStock()

    def show_savings(self, period, user=CUser()):
        """
        Calculates the savings for the specified user in a specified period.
        :param period: string literal year / month / day
        :param user: User to calculate the savings for
        :return: Tuple representing money saved, normal bill and eco bill
        """
        if len(user.power_consumption) == 0:
            return 0

        return self.__calculate_savings(period, user)

    def __calculate_savings(self, period, user):
        """
        Internal method for getting result for show_savings method
        :param period: string literal year / month / day
        :param user: User to calculate savings for
        :return: Tuple representing money saved, normal bill and eco bill
        """
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

        return (normal_bill - eco_bill) / 1000, normal_bill, eco_bill

    def __generated_energy(self, sunlight=4, panel_power=400):
        """
        Calculates generated energy based on number of daylight.
        For simplification, we expect sun light to be const value of 4 hours.
        :param sunlight: The hours of sunlight in a day
        :param panel_power: A wattage of a single solar panel
        :return: Amount of generated energy per day
        """
        return panel_power * sunlight
