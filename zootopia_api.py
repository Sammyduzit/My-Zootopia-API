import requests
from pprint import pprint
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')


def get_animal_data():
    name = 'fox'
    api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(name)
    response = requests.get(api_url, headers={'X-Api-Key': f'{API_KEY}'})
    if response.status_code == requests.codes.ok:
        animal_list = response.json()
        return animal_list
    else:
        print("Error:", response.status_code, response.text)

