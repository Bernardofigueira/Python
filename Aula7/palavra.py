def inverter(palavra):
    return palavra[::-1]


palavra = input("Digite uma palavra: ")
palavra_invertida = inverter(palavra)
print("Palavra original", palavra)
print("Palavra invertida",palavra_invertida)