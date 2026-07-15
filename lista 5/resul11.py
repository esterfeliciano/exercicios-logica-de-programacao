for i in range(10):
    numero = int(input(f"Digite o número {i+1}: "))
    
    if numero < 2:
        continue
    
    primo = True
    for divisor in range(2, numero):
        if numero % divisor == 0:
            primo = False
            break
    
    if primo:
        print(f"{numero} é primo")