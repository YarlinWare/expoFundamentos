import json
import requests

token = "Bearer <TOKEN>"
headers = {"Authorization": token}
r = requests.get('https://rickandmortyapi.com/api/character/', headers = headers)

print('Estado de la comunicación: ',r.status_code,'\n' )
api_r_and_m = r.json()

print(api_r_and_m['results'])