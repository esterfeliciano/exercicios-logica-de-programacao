letra =str(input('Digite uma letra: '))
if letra in 'aeiouAEIOU':
    print('A letra {} é uma vogal'.format(letra))
else:
    print('A letra {} é uma consoante'.format(letra))
