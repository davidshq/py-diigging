import requests
from decouple import config
import os
import os.path
import json

# Pulls from .env
API_AUTHORIZATION_HEADER = config('AUTHORIZATION')
API_USER = config('USER')
API_KEY = config('KEY')

request_url = 'https://secure.diigo.com/api/v2/bookmarks'

def query_basic():
    response = requests.get(
        request_url,
        params={
            'key': API_KEY,
            'user': API_USER,
            'count': 10,
            'start': 50000,
            'filter': 'all'
        },
        headers={
            'Authorization': API_AUTHORIZATION_HEADER,
        }
    )


    json_response = response.json()
    print(response.json())
    print(response.status_code)
    print(response.content)
    save_diigo(json_response)

# Save Diigo data to JSON file.
def save_diigo(json_response):
    file = "diigo.json"
    select_path = ""

    with open(os.path.join(select_path, file), 'a+', encoding='utf-8', errors="replace") as outfile:
        json.dump(json_response, outfile, sort_keys=False, indent=4)

query_basic()