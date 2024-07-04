import requests
import json

URL = "https://ddragon.leagueoflegends.com/cdn/14.13.1/data/en_US/champion.json"

def fetch_json_from_url(URL):
    try:
        response = requests.get(URL)
        response.raise_for_status() # Raise an HTTPError if the HTTP request returned an unsuccessful status code
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"HTTP request failed: {e}")
        return None
    except ValueError as e:
        print(f"Failed to parse JSON: {e}")
        return None

def get_all_champions(_url):
    data = fetch_json_from_url(_url)
    champions = data['data'].keys()
    print(champions)

get_all_champions(_url=URL)

# Fetch and print the JSON data
# lol_champions = fetch_json_from_url(URL)
# if lol_champions:
#     print(json.dumps(lol_champions, indent=4))  # Pretty-print the JSON data
#     print(type(lol_champions))  # Verify the type is a dictionary
    


