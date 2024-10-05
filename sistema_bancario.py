from datetime import datetime
import textwrap

def exibindo_menu():

    menu_texto = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova Conta
    [lc] Listar Contas
    [nu] Novo Usuário
    [q] Sair

    => """
    return input(textwrap.dedent(menu_texto))

def depositar(saldo, valor_deposito, extrato, numero_transacoes, limite_transacoes):
    if numero_transacoes < limite_transacoes:
        if valor_deposito > 0:
            saldo += valor_deposito
            data_atual = datetime.now()
            extrato += f"Depósito de: R$ {valor_deposito:.2f}\nData: {data_atual.strftime('%d/%m/%Y %H:%M')}\n\n"
            numero_transacoes += 1
        else:
            print("Valor do depósito inválido!")
    else:
        print("Número de transações excedido")

    return saldo, valor_deposito, extrato, numero_transacoes

def saque(saldo, valor_sacado, extrato, limite, numero_saques, limite_saques, numero_transacoes, limite_transacoes):
    if numero_transacoes < limite_transacoes:
        excedeu_saldo = valor_sacado > saldo
        excedeu_limite = valor_sacado > limite
        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("Falha no saque! Saldo insuficiente!")
        elif excedeu_limite:
            print("Falha no saque! Limite de saque ultrapassado!")
        elif excedeu_saques:
            print("Falha no saque! Limite de saques diários ultrapassado!")
        elif valor_sacado > 0:
            saldo -= valor_sacado
            data_atual = datetime.now()
            extrato += f"Saque de: R$ {valor_sacado:.2f}\nData: {data_atual.strftime('%d/%m/%Y %H:%M')}\n\n"
            numero_saques += 1
            numero_transacoes += 1
        else:
            print("Falha no saque! Valor informado é inválido!")
    else:
        print("Número de transações excedido")
    
    return saldo, extrato, numero_saques, numero_transacoes

def extraindo_extrato(saldo, extrato):
    print("\n ---------- EXTRATO ----------")
    print("Não foram realizadas movimentações na conta." if not extrato else extrato)
    print(f"\n  Saldo: R$ {saldo:.2f}")
    print("\n -----------------------------")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (Somente número): ")
    usuario = filtrar_usuarios(cpf, usuarios)
    if usuario:
        print("\n Já existe usuário com esse CPF!")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço: ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário criado com sucesso!!!")

def filtrar_usuarios(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios): 
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuarios(cpf, usuarios)
    if usuario:
        print("\n Conta criada com sucesso! ")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\n Usuário não encontrado...")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():

    AGENCIA = "0001"
    LIMITE_SAQUES = 3
    LIMITE_TRANSACOES = 10
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    numero_transacoes = 0
    usuarios = []
    contas = []

    while True:

        opcao = exibindo_menu()

        if opcao == "d" or opcao == "D":
            valor_deposito = float(input("Digite o valor do depósito: "))
            saldo, valor_deposito, extrato, numero_transacoes = depositar(saldo, valor_deposito, extrato, numero_transacoes, LIMITE_TRANSACOES)
        
        elif opcao == "s" or opcao == "S":
            valor_sacado = float(input("Digite o valor que deseja sacar: "))
            saldo, extrato, numero_saques, numero_transacoes = saque(saldo, valor_sacado, extrato, limite, numero_saques, LIMITE_SAQUES, numero_transacoes, LIMITE_TRANSACOES)
        
        elif opcao == "e" or opcao == "E":
            extraindo_extrato(saldo, extrato)

        elif opcao == "nc" or opcao == "NC":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
               contas.append(conta)

        elif opcao == "lc" or opcao == "LC":
            listar_contas(contas)

        elif opcao == "nu" or opcao == "NU":
            criar_usuario(usuarios)

        elif opcao == "q" or opcao == "Q":
            break
        
        else:
            print("Opção Inexistente!")

main()
