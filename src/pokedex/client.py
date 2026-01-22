import requests 

URL = "https://pokeapi.co/api/v2"

def get_pokemon(name_or_id: str | int )-> dict:
    url = f"{URL}/pokemon/{str(name_or_id).lower()}"
    resp = requests.get(url, timeout=10)
    if resp.status_code != 200:
        raise RuntimeError(f"Pokemon no encontrado:{name_or_id} (status{resp.status_code})")
    return resp.json()
