import random

def escolher_dificuldade():
    print("Escolha o nível de dificuldade:")
    print("1 - Fácil (30 tentativas, -10 pontos por erro)")
    print("2 - Médio (15 tentativas, -20 pontos por erro)")
    print("3 - Difícil (5 tentativas, -50 pontos por erro)")

    while True:
        escolha = input("Digite 1, 2 ou 3: ")
        if escolha == '1':
            return 30, 10  # tentativas, perda de pontos
        elif escolha == '2':
            return 15, 20
        elif escolha == '3':
            return 5, 50
        else:
            print("Escolha inválida. Tente novamente.")

def obter_palpite():
    while True:
        try:
            palpite = int(input("Digite seu palpite (entre 10 e 100): "))
            if 10 <= palpite <= 100:
                return palpite
            else:
                print("Número fora do intervalo. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

def jogo_adivinhacao():
    print("Bem-vindo ao Jogo de Adivinhação!")
    tentativas_restantes, perda_por_erro = escolher_dificuldade()
    numero_secreto = random.randint(10, 100)
    pontuacao = 100

    while tentativas_restantes > 0:
        print(f"\nTentativas restantes: {tentativas_restantes} | Pontuação: {pontuacao}")
        palpite = obter_palpite()

        if palpite == numero_secreto:
            print(f"Parabéns! Você adivinhou o número secreto {numero_secreto}!")
            print(f"Sua pontuação final é {pontuacao}.")
            break
        else:
            tentativas_restantes -= 1
            pontuacao -= perda_por_erro
            if palpite < numero_secreto:
                print("Dica: o número secreto é MAIOR.")
            else:
                print("Dica: o número secreto é MENOR.")

    else:
        print(f"\nFim de jogo! O número secreto era {numero_secreto}.")
        print(f"Sua pontuação final é {max(pontuacao, 0)}.")

# Iniciar o jogo
jogo_adivinhacao()
