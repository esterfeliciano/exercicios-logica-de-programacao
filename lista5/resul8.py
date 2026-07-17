contador = 0

for i in range(10):
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    if idade >= 18:
        contador += 1

print(f"Pessoas com 18 anos ou mais: {contador}")