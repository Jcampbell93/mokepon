import requests
import json

from mokepon import Mokepon, ElementalType


def create_mokepon_from_api(name: str):
    res = requests.get('https://pokeapi.co/api/v2/pokemon/'+name)
    pokemon = json.loads(res.text)
    return Mokepon(pokemon["name"], pokemon["stats"][0]["base_stat"], pokemon["stats"][1]["base_stat"], ElementalType(pokemon["types"][0]["type"]["name"]))
