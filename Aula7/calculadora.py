print(20 * "-")
print("Calculadora")
print(20 * "-")

# Coletar o primeiro número
while True:
    numeroUm = input("Digite o primeiro número: ")
    if numeroUm.replace('.', '', 1).isdigit():
        numeroUm = float(numeroUm)
        break
    else:
        print("Digite um número válido!")

# Coletar o segundo número
while True:
    numeroDois = input("Digite o segundo número: ")
    if numeroDois.replace('.', '', 1).isdigit():
        numeroDois = float(numeroDois)
        break
    else:
        print("Digite um número válido!")

# Funções matemáticas
def soma():
    return numeroUm + numeroDois

def subtracao():
    return numeroUm - numeroDois

def divisao():
    if numeroDois != 0:
        return numeroUm / numeroDois
    else:
        return "Divisão por zero"

def multiplicacao():
    return numeroUm * numeroDois

# Escolha da operação
while True:
    print(20 * "-")
    print("Escolha uma operação")
    print(20 * "-")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    operacao = input("Qual você deseja: ")

    if operacao == "1":
        print("O resultado é", soma())
        break
    elif operacao == "2":
        print("O resultado é", subtracao())
        break
    elif operacao == "3":
        print("O resultado é", multiplicacao())
        break
    elif operacao == "4":
        print("O resultado é", divisao())
        break
    else:
        print(20 * "#")
        print("Digite uma opção válida!")
        print(20 * "#")