import requests

new_data = {
  'UserId': 1,
  'id': 1,
  'title': 'Aprondendo Python',
  'body': 'Manipulando Informações da API com Requests'
}

url = 'https://jsonplaceholder.typicode.com/posts/'

posts_response = requests.post(url, json=new_data)
print(posts_response.status_code)