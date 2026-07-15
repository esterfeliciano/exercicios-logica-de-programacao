soma_positivos = 0
qtd_positivos = 0
soma_negativos = 0
qtd_negativos = 0

while True:
    numero = int(input("Digite um número (0 para parar): "))
    
    if numero == 0:
        break
    elif numero > 0:
        soma_positivos += numero
        qtd_positivos += 1
    else:
        soma_negativos += numero
        qtd_negativos += 1

if qtd_positivos > 0:
    print(f"Média dos positivos: {soma_positivos / qtd_positivos}")
else:
    print("Nenhum número positivo foi digitado.")

if qtd_negativos > 0:
    print(f"Média dos negativos: {soma_negativos / qtd_negativos}")
else:
    print("Nenhum número negativo foi digitado.")