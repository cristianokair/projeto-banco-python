conta_bancaria = 0
saques = []
depositos = []
limite_saques = 3
qntos_saques_atuais = 0
LIMITE_POR_SAQUE = 500
msg_falta_saldo = "Não será possível sacar o dinheiro por falta de saldo."


def menu_banco():
    print(
        f"""
        ============= MENU =============

        valor em conta: R$ {conta_bancaria:.2f}

        [d] - Depositar
        [s] - Sacar
        [e] - Extrato
        [q] - Sair

        ================================

        Selecionar opção do menu!

    """
    )


while True:
    menu_banco()
    opcao = input("Opção: ")
    if opcao == "d":
        deposito = 0

        try:
            deposito = float(input("Deposito: "))
        except ValueError:
            print("Valor inválido.")
        
        if deposito <= 0:
            print("valor para depósito não pode ser negativo ou zero")
        else:
            conta_bancaria += deposito
            depositos.append(deposito)
        
    elif opcao == "s":

        if qntos_saques_atuais >= limite_saques:
            print(f"Limite de {limite_saques} saques por dia atingido")
        else:
            saque = 0
            try:
                saque = float(input("Saque: "))
            except ValueError:
                print("Valor inválido.")
            if saque > LIMITE_POR_SAQUE:
                print(f"Valor superior ao limite de R$ {LIMITE_POR_SAQUE:.2f}.")
            elif saque > conta_bancaria:
                print(f"Valor insuficiente em conta.\n -> Saque: R$ {saque:.2f}\n -> Conta: R$ {conta_bancaria:.2f}")
            else:
                qntos_saques_atuais += 1
                conta_bancaria -= saque
                saques.append(saque)
    elif opcao == "e":
        if not len(saques) or not len(depositos):
            print("Não foram realizados movimentações.")
        if len(depositos):
            print("\n#######  DEPÓSITOS #######")
            for deposito in depositos: print(f"R$ {deposito:.2f}")
        if len(saques):
            print("\n#######  SAQUES #######")
            for saque in saques: print(f"R$ -{saque:.2f}")
        print("\n#######  SALDO #######")
        print(f"valor em conta: R$ {conta_bancaria:.2f}")
    elif opcao == "q":
        break
    else:
        print("selecione uma opção válida")