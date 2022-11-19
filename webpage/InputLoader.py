import requests as rek
from json import JSONDecoder

API_HOST = "http://131.159.198.100"
API_PORT = "8000"
API_ENDPOINT = "/contacts/get_users_for_call"

def load_users():
    d = rek.post(f"{API_HOST}:{API_PORT}{API_ENDPOINT}")
    decoder = JSONDecoder()
    res = decoder.decode(d.text)
    return res