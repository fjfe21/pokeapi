import argparse
from src.pokedex.client import get_pokemon

def main():
    parser = argparse.ArgumentParser(description="Mini Pokedex usando PokéAPI")
    parser.add_argument("--pokemon", "-p", required=True, help="Nombre o id del Pokémon (ej: pikachu o 25)")
    args = parser.parse_args()

    data = get_pokemon(args.pokemon)
    print(f"Nombre: {data['name']}")
    print(f"ID: {data['id']}")
    print("Habilidades:")
    for h in data["abilities"]:
        print(" -", h["ability"]["name"])

if __name__ == "__main__":
    main()
