lista_temporia = []
for i in range (5):
    n = int(input('Digite o número {}:' .format(i+1)))
    lista_temporia.append(n)
numeros =list(lista_temporia)
soma_total =sum(numeros)
print('O resultado da soma dos 5 números é: {}' .format(soma_total))