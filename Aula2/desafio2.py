contador = 0

print(150*'-')

numero = int(input('Digite um valor entre 10 e 100: '))
print(150*'-')

if numero<10 or numero>100:
    print('Insira um valor que esteja entre 10 e 100')
else:
    while contador <= numero:
        print("Valor:", contador )
        contador += 1

