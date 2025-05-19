def validar_numero_positivo(valor):
    """Função para garantir que o valor informado seja um número positivo"""
    try:
        valor = float(valor)
        if valor > 0:
            return valor
        else:
            print("O valor deve ser positivo!")
            return None
    except ValueError:
        print("Por favor, digite um número válido!")
        return None

def exibir_menu():
    """Função para exibir o menu de operações"""
    print("\nEscolha uma operação:")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Consultar Saldo")
    print("4 - Consultar Histórico")
    print("5 - Sair")

def main():
    # Solicitação de dados iniciais
    nome_titular = input("Digite o nome do titular da conta: ")
    
    deposito_inicial = None
    while deposito_inicial is None:
        deposito_inicial = validar_numero_positivo(input("Digite o valor do depósito inicial: R$ "))
    
    # Estruturas de dados
    conta = (nome_titular,)  # Tupla com o nome do titular
    saldo = [deposito_inicial]  # Lista com o saldo inicial
    historico = [f"Depósito inicial: R$ {deposito_inicial:.2f}"]  # Lista com o histórico de transações
    
    while True:
        exibir_menu()  # Exibe o menu de operações
        opcao = input("Escolha uma opção: ")

        if opcao == "1":  # Depositar
            valor_deposito = None
            while valor_deposito is None:
                valor_deposito = validar_numero_positivo(input("Digite o valor a ser depositado: R$ "))
            
            saldo[0] += valor_deposito
            historico.append(f"Depósito: R$ {valor_deposito:.2f}")
            print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso.")
        
        elif opcao == "2":  # Sacar
            valor_saque = None
            while valor_saque is None:
                valor_saque = validar_numero_positivo(input("Digite o valor a ser sacado: R$ "))
            
            if valor_saque > saldo[0]:
                print("Saldo insuficiente para realizar o saque!")
            else:
                saldo[0] -= valor_saque
                historico.append(f"Saque: R$ {valor_saque:.2f}")
                print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso.")
        
        elif opcao == "3":  # Consultar saldo
            print(f"Saldo atual: R$ {saldo[0]:.2f}")
        
        elif opcao == "4":  # Consultar histórico
            if historico:
                print("\nHistórico de transações:")
                for transacao in historico:
                    print(transacao)
            else:
                print("Ainda não há transações registradas.")
        
        elif opcao == "5":  # Sair
            print("Obrigado por utilizar nossos serviços!")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
