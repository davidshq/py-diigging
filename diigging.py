import requests
from decouple import config

# Pulls from .env
API_AUTHORIZATION_HEADER = config('AUTHORIZATION')
API_USER = config('USER')
API_KEY = config('KEY')

# Define some constant values
request_url = 'https://secure.diigo.com/api/v2/bookmarks'

# Basic Query Returns 10 Bookmarks
def basic_query():
    response = requests.get(
        request_url,
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

# Query Through Multiple Pages
def query_multiple_pages():
    page_number = 1
    response = requests.get(
        request_url,
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


# Uncomment line below to run basic_query
# basic_query()