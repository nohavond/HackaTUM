import random

LIST_OF_OFFERS = [
    {
        "name": "Let's go solar!",
        "startin_eur_price": 125,
        "image_url": "something.com/image.jpg"},
    {
        "name": "Beautiful kitchen",
        "starting_eur_price": 200,
        "image_url": "something.jpg"
    },
    {
        "name": ""
    }
]


class PackageOffers:
    """
    Class for retrieving package offers for the users.
    """

    def __init__(self):
        pass

    def get_package_offers(self):
        return

    def generate_kitchen(self):
        for i in range(40):
            price = random.randrange(1200, 2000)
