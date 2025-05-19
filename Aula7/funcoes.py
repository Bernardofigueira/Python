"""
    O que é funções?
        ->As funcoes sao blocos de codigo que realizam uma tarefa
        ->Esses codigos são reutilizaveis
        ->Ajudam a organizar o codigo
        ->Ajuda a não repetir codigos desnecessariamente

"""

#Sintaxe (Escrita) da função
def nome_funcao():

    """ Corpo da funcao
    Comandos da função """

#def- Palavra chave para definir a função
#nome_funcao() - Nome que identifica a função

print("Função Simples")
def saudacao():
    print("Olá! Boa noite Ass:Bonner")

#Precisamos chamar a função
saudacao() 

print(20* "-")
print("Função com parametros")

def saudacao_turma(nome_turma):
    print("Boa Noite!!!", nome_turma)

saudacao_turma("2025.1 Top")
saudacao_turma("Galera")

print(20*"-")
print("Função com retorno")
def soma():
    return 1 + 2

print("O resultado é:",soma())