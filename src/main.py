from CSolar import CSolar
from CUser import CUser
from CStock import CStock


def main():
    dummy_user = CUser()
    dummy_user.generate_data()

    stock = CStock()
    solar = CSolar()
    solar.show_savings('today', dummy_user)


if __name__ == "__main__":
    main()
