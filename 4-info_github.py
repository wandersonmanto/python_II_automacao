import requests
from collections import Counter
import pandas

base_api = 'https://api.github.com'
owner = 'wandersonmanto'
url = f"{base_api}/users/{owner}/repos"

list_repositorios = []
list_language = []

response = requests.get(url)
print(response.status_code)
print(len(response.json()))
for repo in response.json():
  print(repo['full_name'])
  print(repo['language'], '\n')
  list_repositorios.append(repo['full_name'])
  list_language.append(repo['language'])
  
print(Counter(list_language))

# Crianda data frame
dados_git = pandas.DataFrame()
dados_git['repositorios'] = list_repositorios
dados_git['linguagens'] = list_language
print(dados_git)

# Exportar csv
dados_git.to_excel('git.xlsx')
