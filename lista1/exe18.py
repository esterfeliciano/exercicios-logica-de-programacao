##Peça ao usuário a quantidade de dias, horas, minutos e segundos e converta tudo para segundos.
dias = int(input('Digite a quantidade de dias: '))
horas = int(input('Digite a quantidade de horas: '))
minutos = int(input('Digite a quantidade de minutos: '))
segundos = int(input('Digite a quantidade de segundos: '))
total_segundos = dias * 24 * 60 * 60 + horas * 60 * 60 + minutos * 60 + segundos
print('O total de segundos é: {}'.format(total_segundos))