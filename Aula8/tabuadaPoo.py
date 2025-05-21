class Tabuada:
    def __init__(self, numero):
        self.numero = numero  # Atributo público
        self.__resultado = 0 # Atributo privado
    def soma(self):
        for i in range(1,11):
            self.__resultado = self.numero + i
            print(self.numero,"+",i,"=",self.__resultado)

    def multiplicacao(self):
        for i in range(1,11):
            self.__resultado = self.numero * i
            print(self.numero,"x",i,"=",self.__resultado)

    def divisao(self):
        if self.numero > 0:
            for i in range(1,11):
                self.__resultado = self.numero / i
                print(self.numero,"/",i,"=",self.__resultado)
        else:
            print("Divisão por zero")
    def subtracao(self):
        for i in range(1,11):
            self.__resultado = self.numero - i
            print(self.numero,"-",i,"=",self.__resultado)     