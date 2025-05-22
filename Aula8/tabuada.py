from tabuadaPoo import Tabuada


while True:
    print(20*"#")
    numeroUm = input("Digite um número:")
    print(20*"#")
    print("")
    if numeroUm.strip().replace('.', '', 1).isdigit():
        numero = float(numeroUm)
        break
    else:
        print(20*"#")
        print("Digite um número válido!")
        print(20*"#")
    print("")   
tabuada_um = Tabuada(numero)
print(20*"-")
print("Tabuada da soma")
print(20*"-")
print("")
tabuada_um.soma()


print("")
print(20*"-")
print("Tabuada da Multiplicação")
print(20*"-")
print("")

tabuada_um.multiplicacao()


print("")
print(20*"-")
print("Tabuada da divisao")
print(20*"-")
print("")

tabuada_um.divisao()


print("")
print(20*"-")
print("Tabuada da subtração")
print(20*"-")
print("")

tabuada_um.subtracao()
print("")