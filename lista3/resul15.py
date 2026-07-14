##Peça um número e diga se ele está nos intervalos [0,25], (25,50], (50,75] ou (75,100].
n =int(input('Digite um número: '))
if n >=0 and n <=25:
    print('O número está no intervalo [0,25]')
elif n > 25 and n <=50:
    print('O número está no intervalo (25,50]')
elif n > 50 and n <=75:
    print('O número está no intervalo (50,75]')
else:
    print('O número está no intervalo (75,100]')