n = int(input("Quantos números você vai digitar? "))
contador = 0

for i in range(n):
    numero = int(input(f"Digite o número {i+1}: "))
    if numero % 3 == 0:
        contador += 1

print(f"Quantidade de múltiplos de 3: {contador}")