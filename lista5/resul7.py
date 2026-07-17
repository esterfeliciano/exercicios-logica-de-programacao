contador_pares = 0

while True:
    numero = int(input("Digite um número (negativo para parar): "))
    if numero < 0:
        break
    if numero % 2 == 0:
        contador_pares += 1

print(f"Quantidade de números pares digitados: {contador_pares}")