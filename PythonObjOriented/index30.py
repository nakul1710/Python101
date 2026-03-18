# Api using python
import requests

base_url = "https://pokeapi.co/api/v2/"
 

def get_pokemon_data(pokemon_name):
    url = f"{base_url}pokemon/{pokemon_name.lower()}"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()

pokemon_name = "Pikachu"
data = get_pokemon_data(pokemon_name)    
print(data["name"], "id:", data["id"])
