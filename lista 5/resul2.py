contador = 0

for i in range(10):
    numero = int(input(f"Digite o número {i+1}: "))
    if numero > 100:
        contador += 1

print(f"Quantidade de números maiores que 100: {contador}")