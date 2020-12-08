import requests
from decouple import config

# Pulls from .env
API_AUTHORIZATION_HEADER = config('AUTHORIZATION')
API_USER = config('USER')
API_KEY = config('KEY')

# Basic Query
response = requests.get(
    'https://secure.diigo.com/api/v2/bookmarks',
    params={
        'key': API_KEY,
        'user': API_USER,
        'count': 10,
        'filter': 'all'
    },
    headers={
        'Authorization': API_AUTHORIZATION_HEADER,
    }
)

json_response = response.json()
print(json_response)