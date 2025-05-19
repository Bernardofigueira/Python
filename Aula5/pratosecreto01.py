pratos = ['Lasanha','Macarrão','Moela','Feijoada','Podrão','Kibe']
import random
pratoSecreto = random.choice(pratos)
print(pratoSecreto)

print(25*"#")
print("Descubra o prato secreto")
print(25*"#")
print("")
print(43*"#")
print("Você é capaz de descobrir o prato secreto?")
print(43*"#")
print('Qual dificuldade você quer jogar?')
print("1 - Fácil (30 tentativas)")
print("2 - Médio (15 tentativas)")
print("3 - Difícil (5 tentativas")
dificuldade= input('Digite 1,2 ou 3: ')
tentativa = 1

if(dificuldade == '3'):
    tentativas = 5
    erro = 50
    tentar = 5

elif (dificuldade == '2'):
    tentativas = 15
    erro = 20
    tentar = 15

elif(dificuldade == '1'):
    tentativas = 30
    erro = 10
    tentar = 30
else:
    print(43*"#")
    print('Insira uma dificuldade válida')
    print(43*"#")
    exit()

while tentativas > 0:   
    print(43*'-')
    print(f"Tentativa {tentativa} de {tentar} ")
    print(43*'-')

    palpite = input("Informe um prato : ") 
    print("")
    
    print("Seu palpite é: {}".format(palpite))
    if pratoSecreto.lower() == palpite.lower():
        print(150*"#")
        print("Você acertou miseravi")
        print('')
        break #Encerra o jogo (Encerra o if e a repetição)
    else:
        print("Você errou miseravi")
    
    tentativa += 1
    tentativas -= 1
    

print(150*"#")
print("Fim de jogo")
print('O prato secreto era',pratoSecreto)
print(150*"#")