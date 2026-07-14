n1 = int(input("Digite um número: "))
multiplo_2 = n1 % 2 == 0
multiplo_3 = n1 % 3 == 0
if not multiplo_2 and not multiplo_3:
    print("O número não é múltiplo de 2 nem de 3.")     
    