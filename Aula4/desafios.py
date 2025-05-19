"""
    Desafio 01: Soma dos Elementos: Dada a lista de numeros inteiros numeros = [10,20,30,40,50] calcule e imprima a soma de todos os seus elementos.


"""
#Declarando a lista
numeros = [10,20,30,40,50]
soma = 0

for numero in numeros:
    soma += numero
    print(soma)
print('A soma dos elementos é', soma)
