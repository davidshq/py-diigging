import requests
from decouple import config
import os
import os.path
import json

# Pulls from .env
API_AUTHORIZATION_HEADER = config('AUTHORIZATION')
API_USER = config('USER')
API_KEY = config('KEY')

# Define some constant values
request_url = 'https://secure.diigo.com/api/v2/bookmarks'

# Basic Query Returns 10 Bookmarks
def query_basic():
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
    save_diigo(json_response)


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

# Query Through All Pages
def query_all_pages():
    counter_per_page = 100
    filter_options = 'all'
    bookmark_number = 1
    response_404 = 0
    while response_404 != 404:
        all_response = requests.get(
            request_url,
            params={
                'key': API_KEY,
                'user': API_USER,
                'count': counter_per_page,
                'filter': filter_options,
                'start': bookmark_number,
            },
            headers={
                'Authorization': API_AUTHORIZATION_HEADER,
            }
        )

        json_response = all_response.json()
        # print(json_response)
        save_diigo(json_response)
        bookmark_number +=100
        if all_response.status_code == 404:
            response_404 = 404

        # For testing, to avoid actually pulling all pages
        # if page_number == 3:
        #    break

# Save Diigo data to JSON file.
def save_diigo(json_response):
    file = "diigo.json"
    select_path = ""

    with open(os.path.join(select_path, file), 'a+', encoding='utf-8', errors="replace") as outfile:
        json.dump(json_response, outfile, sort_keys=False, indent=4)

# Uncomment desired query below.
# query_basic()
# query_multiple_pages()
query_all_pages() 
