import requests

# print(requests.__version__)
# print(dir(requests))

# Requisição com GET
link = 'https://www.google.com.br/search?q=Palmeiras'
response = requests.get(link)

if response.status_code == 200:
  response_json = response.json()
  print(response_json)