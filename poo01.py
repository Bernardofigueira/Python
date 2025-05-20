#Criando nosso primeiro modelo (CLasse)
class Cachorro:

    #Atributos (Variaveis Metidas)
    raca = ""
    nome = ""
    idade = 0

    #Método (Funçoes metidas)
    def latir(self):
        print("Au Au!")


#Usa o modelo (Instancia)
cachorro_um = Cachorro()

cachorro_um.raca = "Vira-Lata"
cachorro_um.nome = "Bruno Henrique"

print(f"A raça do meu cachorro é: {cachorro_um.raca}")
cachorro_um.latir()


cachorro_dois = Cachorro()
cachorro_dois.raca = "Husky"
cachorro_dois.nome = "Gabigol"
cachorro_dois.latir()
print(f"O nome do cachorro é: {cachorro_dois.nome}")
