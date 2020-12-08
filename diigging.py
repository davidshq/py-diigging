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
    max_page_number = 10
    counter_per_page = 10
    filter_options = 'all'
    page_number = 1
    while page_number <= max_page_number:
        multiple_response = requests.get(
            request_url,
            params={
                'key': API_KEY,
                'user': API_USER,
                'count': counter_per_page,
                'filter': filter_options,
                'start': page_number,
            },
            headers={
                'Authorization': API_AUTHORIZATION_HEADER,
            }
        )

        json_response = multiple_response.json()
        print(json_response)
        page_number +=1


# Uncomment line below to run basic_query
# basic_query()

# Uncomment line below to run query_multiple_pages
query_multiple_pages()