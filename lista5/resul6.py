contador = 0

for i in range(10):
    numero = float(input(f"Digite o número {i+1}: "))
    if 10 <= numero <= 20:
        contador += 1

print(f"Quantidade de números entre 10 e 20: {contador}")