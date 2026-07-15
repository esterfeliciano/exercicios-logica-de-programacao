temperaturas = {
    "Recife": 30,
    "São Paulo": 22,
    "Curitiba": 15,
    "Manaus": 34,
    "Porto Alegre": 18
}

cidade_mais_quente = max(temperaturas, key=temperaturas.get)

print(f"A cidade mais quente é {cidade_mais_quente}, com {temperaturas[cidade_mais_quente]}°C")