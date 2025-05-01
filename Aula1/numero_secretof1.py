print(150*'-')
print('Descubra o número secreto')
print(150*'-')
print('')

numeroSecreto = 7
numero = int(input ('Digite um número:'))
if numeroSecreto == numero: print ('Parabéns, você acertou o número secreto!')
elif numeroSecreto > numero: print('Errou! O número secreto é maior que ',numero)
else: print('Errou! O número secreto é menor que', numero) 