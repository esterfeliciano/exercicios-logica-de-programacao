n = int(input("Digite um número: "))

soma = 0
for numero in range(1, n + 1):
    if numero % 2 != 0:
        soma += numero

print(f"Soma dos ímpares entre 1 e {n}: {soma}")