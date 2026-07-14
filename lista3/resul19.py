n1 =float(input("Digite o primeiro numero: "))
n2 =float(input("Digite o segundo numero: "))
operador = input("Digite o operador (+, -, *, /): ")
if operador == '+':
    resultado = n1 + n2
    print('O resultado da soma é: {}'.format(resultado))
elif operador == '-':
    resultado = n1 - n2
    print('O resultado da subtração é: {}'.format(resultado))
elif operador == '*':
    resultado = n1 * n2
    print('O resultado da multiplicação é: {}'.format(resultado))
elif operador == '/':
    resultado = n1 / n2
    print('O resultado da divisão é: {}'.format(resultado))
else:
    print('Operador inválido.')
    
