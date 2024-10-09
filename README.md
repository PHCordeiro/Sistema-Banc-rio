
# Sistema Bancário

Este é um sistema bancário simples que permite a um único usuário realizar operações como depósito, saque e consulta de extrato.

## Funcionalidades

### Menu

O sistema apresenta um menu interativo com as seguintes opções:

### Depositar

Permite ao usuário depositar um valor na conta. Se o valor for válido (positivo), ele é adicionado ao saldo e registrado no extrato.

### Sacar

Permite ao usuário sacar um valor da conta. Se o valor for válido, não exceder o saldo disponível, o limite de saque diário (R$ 500) ou o número máximo de saques permitidos (3 por dia), ele é subtraído do saldo e registrado no extrato.

### Extrato

Exibe todas as movimentações da conta, incluindo depósitos e saques, além do saldo atual. Caso não haja movimentações, uma mensagem informando isso será exibida.

### Nova Conta

Cria uma nova conta para um usuário existente. O sistema solicita o CPF do usuário, que deve estar previamente cadastrado, para vincular a nova conta ao cliente.

### Listar Contas

Exibe todas as contas criadas no sistema, mostrando as informações da agência, número da conta e o titular.

### Novo Usuário

Permite registrar um novo usuário no sistema. O sistema solicita as seguintes informações: nome, CPF, data de nascimento e endereço.

### Sair

Encerra o programa.

## Regras

- **Limite de saques diários**: 3 saques por dia.
- **Limite total de transações**: O sistema permite registrar até 10 transações por conta.
- **Limite máximo de saque**: R$ 500 por saque.

## Exemplo de Uso

No início, o sistema exibe o menu com as opções listadas acima. O usuário deve digitar a letra correspondente à operação que deseja realizar. Por exemplo, para realizar um depósito, o usuário digita `d`, insere o valor do depósito e o sistema processa a operação. 

Da mesma forma, o usuário pode escolher sacar (`s`), ver o extrato (`e`), criar uma nova conta (`nc`), listar as contas (`lc`), adicionar um novo usuário (`nu`), ou sair do sistema (`q`).

## Observações Técnicas

- O sistema implementa o conceito de transações abstratas usando a classe base `Transacao` e suas subclasses `Saque` e `Deposito`, garantindo que todas as operações financeiras sejam registradas corretamente no histórico da conta.
- O histórico de cada conta é armazenado em uma lista de transações dentro da classe `Historico`, com cada transação registrando o tipo, valor e data/hora.
- A arquitetura foi organizada para permitir fácil extensão, como a adição de novos tipos de contas ou regras de negócio no futuro.
