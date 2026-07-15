produtos = {}

for i in range(3):
    print('Cadastro do produto {}' .format(i+1))
    nome =str(input('Digite o nome: '))
    preco =float(input('Digite o preço:'))

    produtos[nome]=preco

mais_caro = max(produtos, key=produtos.get)
preco_mais_caro = produtos[mais_caro]

print('O produto mais caro é o {}. ' .format(mais_caro))