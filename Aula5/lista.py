frutas = ['Maçã','Banana','Laranja','Pera','Abacaxi']
print(frutas[2])#Exibe um item da lista
print(frutas[-1])#Lê o ultimo
print(frutas[-2])#lê o penultimo

print(20*'-')

#Cortar - Slice
print(frutas[0:2])#Exibe os valores de indice 0 e 1 e corta do indice 2
print(frutas[1:3])#Exibe os valores de indice 1 e 2 e corta o indice 3
print(frutas[:])#Exibe todos os elementos
print(frutas[::2])#Exibe os numeros pares

#tamanho len()
print(len(frutas))

#Concatenaro - JUntar (+)
mais_frutas = ["morango","uva"]
cesta_de_frutas = frutas + mais_frutas
print(cesta_de_frutas)

#Repetire o array
repita = frutas *3
print (repita)

#Adicionando elementos
frutas.append("goiaba")#Adiciona um elemento ao final da lista
print(frutas)

frutas.insert(0,"melao") #ADiciona um elemento em uma posicao especifica
print(frutas)

frutas_dois = ['tomate', 'kiwi']
frutas.extend(frutas_dois)#mais elementos na lista
print(frutas)
frutas.insert(2,frutas_dois)
print(frutas)

#Removendo dados da lista 
frutas.remove('melao')
print(frutas)

elemento = frutas.pop(2)
print(frutas)#Exibe o array sem o elemento retirado pelo pop
print( elemento)#Exibe somemte o elemento