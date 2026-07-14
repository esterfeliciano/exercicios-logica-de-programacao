n = int(input('Digite um número: '))
if n < 2:
    print('O número não é primo.')  
else:
    primo = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            primo = False
            break
    if primo:
        print('O número é primo.')
    else:
        print('O número não é primo.')