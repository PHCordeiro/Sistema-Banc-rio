# Sistema Bancário
Este é um sistema bancário simples, que permite a um único usuário realizar operações como depósito, saque e consulta de extrato.

## Funcionalidades
## Menu
O sistema apresenta um menu interativo com as seguintes opções:
## Depositar 
Permite ao usuário depositar um valor na conta. Se o valor for válido, ele é adicionado ao saldo e registrado no extrato.
## Sacar 
Permite ao usuário sacar um valor da conta. Se o valor for válido e não exceder o saldo, o limite de saque ou o número máximo de transações, ele é subtraído do saldo e registrado no extrato.
## Extrato 
Exibe todas as movimentações da conta, incluindo depósitos e saques, além do saldo atual.
## Nova Conta 
Cria uma nova conta para um usuário existente, solicitando o CPF do usuário.
## Listar Contas 
Exibe todas as contas criadas com informações sobre a agência, número da conta e titular.
## Novo Usuário 
Permite registrar um novo usuário, solicitando informações como nome, CPF, data de nascimento e endereço.
## Sair 
Encerra o programa.
## Regras
 - Limite de saques diários: 3
 - Limite total de transações: 10
 - Limite máximo de saque: R$ 500
