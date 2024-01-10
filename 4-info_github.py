import requests

base_api = 'https://api.github.com'
owner = 'wandersonmanto'
url = f"{base_api}/users/{owner}/repos"

response = requests.get(url)
print(response.status_code)
print
