import requests

url = 'https://jsonplaceholder.typicode.com/posts/1'
response = requests.get(url)

if response.status_code == 200:
  response_json = response.json()
  print(response_json)
  
# Adicionando payload
payload = {
  "id": [1, 2, 3, 4, 5],
  "userId": 1
}

url = 'https://jsonplaceholder.typicode.com/posts/'

# Realizando requisição
response = requests.get(url, params=payload)
for i in response.json():
  print(i, '\n')