from CSolar import CSolar
from CUser import CUser
from CStock import CStock
import datetime
import random
import json


def main():
    dummy_user = CUser()
    dummy_user.generate_data()

    dummy_user2 = CUser()
    dummy_user2.generate_data()

    solar = CSolar()
    solar.show_savings('today', dummy_user)
    solar.show_savings('today', dummy_user2)


if __name__ == "__main__":
    main()
