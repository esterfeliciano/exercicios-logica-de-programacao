lista_temporia = []
for i in range (4):
    n = float(input('Digite uma nota {}:' .format(i+1)))
    lista_temporia.append(n)
notas =list(lista_temporia)
soma_total =sum(notas)

media = soma_total/4
print('A média é : {}' .format(media))