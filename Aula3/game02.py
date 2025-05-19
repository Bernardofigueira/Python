print(25*"#")
print("Descubra o numero secreto")
print(25*"#")
print("")
print(43*"#")
print("Você é capaz de descobrir o numero secreto?")
print(43*"#")
import random
secreto_num = random.randint(10,100)
print('Qual dificuldade você quer jogar?')
print("1 - Fácil (30 tentativas, -10 pontos por erro)")
print("2 - Médio (15 tentativas, -20 pontos por erro)")
print("3 - Difícil (5 tentativas, -50 pontos por erro)")
dificuldade= input('Digite 1,2 ou 3: ')
tent_dificil = 5
tent_medio = 15
tent_facil = 30
pontuação = 100
tentativa = 1

if(dificuldade == '3'):
    tentativas = tent_dificil
    erro = 50
    tentar = tent_dificil

elif (dificuldade == '2'):
    tentativas = tent_medio
    erro = 20
    tentar = tent_medio

elif(dificuldade == '1'):
    tentativas = tent_facil
    erro = 10
    tentar = tent_facil
else:
    print(43*"#")
    print('Insira uma dificuldade válida')
    print(43*"#")
    exit()


while tentativas > 0:   
    print(43*'-')
    print(f"Tentativa {tentativa} de {tentar}  ||    Seus Pontos : {pontuação}")
    print(43*'-')

    if(pontuação <= 0): #Caso os pontos cheguem a 0 ele encerra o jogo
        print(150*"#")
        print('Seus pontos acabaram')
        break

    palpite = int(input("Informe um número entre 10 e 100: ")) #Converter para inteiro
    print("")
    if palpite < 10 or palpite > 100:
        print(43*"#")
        print('Informe um número valido!')
        print(43*"#")
        continue
    
    print("Seu palpite é: {}".format(palpite))
    if secreto_num == palpite:
        print(150*"#")
        print("Você acertou miseravi")
        print('')
        print('Total de Pontos',pontuação)
        break #Encerra o jogo (Encerra o if e a repetição)
    else:
        print("Você errou miseravi")
        pontuação -= erro
    
    tentativa += 1
    tentativas -= 1

print(150*"#")
print("Fim de jogo")
print('O número secreto era',secreto_num)
print(150*"#")