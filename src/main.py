from CSolar import CSolar
from CUser import CUser


def main():
    dummy_user = CUser()
    dummy_user.generate_data()

    data = dummy_user.get_consumption('today')
    for date, watts in data.items():
        print(date, watts)

    solar = CSolar()


if __name__ == "__main__":
    main()
