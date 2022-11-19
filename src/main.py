from CSolar import CSolar
from CUser import CUser


def main():
    dummy_user = CUser()
    dummy_user.generate_data()

    solar = CSolar()
    solar.show_savings('today')


if __name__ == "__main__":
    main()
