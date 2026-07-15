chaves = {}

for i in range(3):
    print('Cadastro de chaves {}' .format(i+1))
    nome =str(input('Digite o nome da chave: '))
    valor =int(input('Digite a o valor da chave: '))

    chaves[nome]=valor
    c =dict(chaves)

print('As chaves criadas foram{}' .format(c)) 