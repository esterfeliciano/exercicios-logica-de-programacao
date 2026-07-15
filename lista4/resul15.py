pessoas = {
    "Ana": 22,
    "Bruno": 15,
    "Carla": 30,
    "Diego": 17,
    "Elisa": 19
}

for nome, idade in pessoas.items():
    if idade > 18:
        print(nome)