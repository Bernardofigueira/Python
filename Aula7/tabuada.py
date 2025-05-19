def tabuada():
    for i in range(1,11):
        resultado = numero * i
        print(numero,"x",i,"=",resultado)
while True:
    numero = (input("Digite o número da tabuada desejada: "))
    if numero.isdigit():
        numero = int(numero)
        tabuada()
        break
    else:
        print("Digite um número válido")
