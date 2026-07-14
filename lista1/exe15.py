valor_produto = float(input('Digite o valor do produto: '))
num_parcelas = int(input('Digite o número de parcelas: '))
valor_parcela = valor_produto / num_parcelas
print('O valor de cada parcela é: {:.2f}'.format(valor_parcela))