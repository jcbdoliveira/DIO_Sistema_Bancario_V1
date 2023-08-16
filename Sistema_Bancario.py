import time

menu = """
    =========BEM VINDO AO DIO BANK=======
    Selecione una operação:    

    [d] Depositar Valor
    [s] Sacar Valor
    [e] Consultar Extrato
    [x] Encerrar Operação

    => """

seu_saldo = 0
limite_saque = 500
seu_extrato = ""
qtde_saques = 0
SAQUES_POR_DIA = 3

while True:
    
    opcao = input(menu)

    if opcao == "d":
        valor_operacao = float(input("Informe o valor à ser depositado: "))

        if valor_operacao > 0:
            seu_saldo += valor_operacao
            seu_extrato += f"Depósito: R$ {valor_operacao:.2f}\n"
            print("Operação realizada com sucesso!")
            time.sleep(3)
        else:
            print("Operação falhou! Valor informado inválido")
            time.sleep(5)
    
    elif opcao == "s":
        valor_operacao = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor_operacao > seu_saldo

        excedeu_limite = valor_operacao > limite_saque

        excedeu_saques = qtde_saques >= SAQUES_POR_DIA

        if excedeu_saldo:
            print("=============== ATENÇÃO ===============\nFalha na operação!\nVocê não tem saldo suficiente.\n=======================================")
            time.sleep(5)

        elif excedeu_limite:
            print("=============== ATENÇÃO ===============\nFalha na operação!\nO valor do saque excede o limite de saque único.\n=======================================")
            time.sleep(5)

        elif excedeu_saques:
            print("=============== ATENÇÃO ===============\nFalha na operação!\nNúmero máximo de saques excedido.\n=======================================")
            time.sleep(5)
        
        elif valor_operacao > 0:

            seu_saldo -= valor_operacao
            seu_extrato += f"Saque...: R$ {valor_operacao:.2f}\n"                             
            qtde_saques += 1
            print("Operação realizada com sucesso!")
            time.sleep(3)
        else:
            print("=============== ATENÇÃO ===============\nFalha na operação!\nO valor informado é inválido.\n=======================================")
            time.sleep(5)

    elif  opcao == "e":
        print("\n=============== EXTRATO ===============")
        print("\nNão foram realizadas movimentações." if not seu_extrato else seu_extrato)
        print(f"\nSaldo...: R$ {seu_saldo:.2f}")
        print("\n=======================================")
        time.sleep(5)
    elif opcao == "x":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        time.sleep(3)