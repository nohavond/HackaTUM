import random

LIST_OF_OFFERS = [
    {
        "name": "Let's go solar",
        "startin_eur_price": 125,
        "image_url": "https://images.pexels.com/photos/9875418/pexels-photo-9875418.jpeg?auto=compress&cs=tinysrgb&w=1200&dpr=1"
    },
    {
        "name": "Cooking time",
        "starting_eur_price": 200,
        "image_url": "https://images.pexels.com/photos/2724749/pexels-photo-2724749.jpeg?auto=compress&cs=tinysrgb&w=1200&dpr=1"
    },
    {
        "name": "Sunshine",
        "starting_eur_price": 180,
        "image_url": "https://images.pexels.com/photos/3889873/pexels-photo-3889873.jpeg?auto=compress&cs=tinysrgb&w=1200&dpr=1"
    },
    {
        "name": "Cinema experience",
        "starting_eur_price": 40,
        "image_url": "https://images.pexels.com/photos/7991426/pexels-photo-7991426.jpeg?auto=compress&cs=tinysrgb&w=1200"
    },
    {
        "name": "Good night",
        "starting_eur_price": 55,
        "image_url": "https://images.pexels.com/photos/1329711/pexels-photo-1329711.jpeg?auto=compress&cs=tinysrgb&w=1200"
    },
    {
        "name": "New workshop",
        "starting_eur_price": 95,
        "image_url": "https://images.pexels.com/photos/162553/keys-workshop-mechanic-tools-162553.jpeg?auto=compress&cs=tinysrgb&w=1200"
    },
    {
        "name": "Wellness",
        "starting_eur_price": 70,
        "image_url": "https://images.pexels.com/photos/3288104/pexels-photo-3288104.png?auto=compress&cs=tinysrgb&w=1200"
    },
    {
        "name": "Safety first",
        "starting_eur_price": 80,
        "image_url": "https://images.pexels.com/photos/430208/pexels-photo-430208.jpeg?auto=compress&cs=tinysrgb&w=1200&dpr=1"
    },
    {
        "name": "Garden fun",
        "starting_eur_price": 120,
        "image_url": "https://images.pexels.com/photos/334978/pexels-photo-334978.jpeg?auto=compress&cs=tinysrgb&w=1200&dpr=1"
    },
    {
        "name": "Garage upgrade",
        "starting_eur_price": 200,
        "image_url": "https://images.pexels.com/photos/4480505/pexels-photo-4480505.jpeg?auto=compress&cs=tinysrgb&w=1200&dpr=1"
    },
    {
        "name": "Wine cellar",
        "starting_eur_price": 120,
        "image_url": "https://images.pexels.com/photos/2664150/pexels-photo-2664150.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=1200"
    }
]


class PackageOffers:
    """
    Class for retrieving package offers for the users.
    """

    def __init__(self):
        pass

    def get_package_offers(self):
        random.shuffle(LIST_OF_OFFERS)
        return LIST_OF_OFFERS[:10]
