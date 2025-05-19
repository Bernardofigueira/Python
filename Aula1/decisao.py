"""
    Estrutura de decisão
    Classificação
        >Simples
        >Composta
        >Encadeada
        >Aninhada
"""
print('Decisão Simples - é dada por uma única resposta')
idade = 18
if idade >= 18:
    print('Maior de idade')

print(15*"-")

print('Composta - uma unica decisao e uma resposta padrão')

if idade >= 18:
    print('Maior de idade')
else:
    print('Infelizmente não posso te ajudar')

print(15*"-")

print('Encadeada - é dada por mais de uma decisão e uma resposta padrão')

if idade >= 18:
    print('Maior de idade')
elif idade<=18:
    print('Maior de idade')
else:
    print('Infelizmente não posso te ajudar')

print(15*"-")

print('Aninhada - Possui uma estrutura de decisão dentro da outra')
classificacao = 16
ingresso = False

if classificacao >=16:
    if ingresso == True:
        print('Você pode assistir ao filme')
    else:
        print('Você não pode assistir ao filme')
else:
    print('Você não pode assistir ao filme')