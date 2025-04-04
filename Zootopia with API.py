import requests
from pprint import pprint

name = 'fox'
api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(name)
response = requests.get(api_url, headers={'X-Api-Key': 'EvshZpIZFESeEJBXVPBVWA==q2RhOZnU0Uph2Pgf'})
if response.status_code == requests.codes.ok:
    json = response.json()
    pprint(json)
    print(response.status_code)
else:
    print("Error:", response.status_code, response.text)

