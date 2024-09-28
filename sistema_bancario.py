menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("Digite o valor do depósito: "))

        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"   Depósito de: R$ {valor_deposito:.2f}\n"
        else:
            print("Valor do depósito inválido!")
    
    elif opcao == "s":
        valor_sacado = float(input("Digite o valor que deseja sacar: "))
        excedeu_saldo = valor_sacado > saldo
        excedeu_limite = valor_sacado > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Falha no saque! Saldo insuficiente!")
        elif excedeu_limite:
            print("Falha no saque! Limite de saque ultrapassado!")
        elif excedeu_saques:
            print("Falha no saque! Limite de saques diários ultrapassado!")
        elif valor_sacado > 0:
            saldo -= valor_sacado
            extrato += f"   Saque de: R$ {valor_sacado:.2f}\n"
            numero_saques += 1
        else:
            print("Falha no saque! Valor informado é inválido!")
    
    elif opcao == "e":
        print("\n ---------- EXTRATO ----------")
        print("Não foram realizadas movimentações na conta." if not extrato else extrato)
        print(f"\n  Saldo: R$ {saldo:.2f}")
        print("\n -----------------------------")
    elif opcao == "q":
        break
    else:
        print("Opção Inexistente!")

        