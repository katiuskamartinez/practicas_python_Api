import requests

URL= "https://pokeapi.co/api/v2/pokemon/"

pokemon= input("nombra un pokemon: ")

respuesta= requests.get(URL + pokemon)

datos= respuesta.json()

print(f"----movimientos de {pokemon}  ----")
for move in datos["moves"]:
  print(move["move"]["name"])

print(f"---Tipos de {pokemon} ---")
for type in datos["types"]:
  print(type["type"]["name"])

