pessoas = {}

for i in range(10):
    nome = input(f"Nome da pessoa {i+1}: ")
    idade = int(input(f"Idade de {nome}: "))
    pessoas[nome] = idade

mais_velha = max(pessoas, key=pessoas.get)
mais_nova = min(pessoas, key=pessoas.get)

print(f"Mais velha: {mais_velha} ({pessoas[mais_velha]} anos)")
print(f"Mais nova: {mais_nova} ({pessoas[mais_nova]} anos)")