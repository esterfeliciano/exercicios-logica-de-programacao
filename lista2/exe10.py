n1 = int(input("Digite um número: "))
multiplo_3 = n1 % 3 == 0
multiplo_7 = n1 % 7 == 0                
if multiplo_3 or multiplo_7:
    print("O número é múltiplo de 3 ou de 7.")  
