# Função para criar usuário
def criar_usuario(nome, data_nascimento, cpf, endereco, usuarios):
    cpf = ''.join(filter(str.isdigit, cpf))  # Remover tudo, exceto os números do CPF
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("Erro! Usuário com esse CPF já existe.")
            return
    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})
    print(f"Usuário {nome} criado com sucesso!")

# Função para criar conta corrente
def criar_conta_corrente(cpf, contas, usuarios):
    conta_numero = len(contas) + 1
    agencia = "0001"
    
    # Buscar usuário pelo CPF
    usuario_encontrado = None
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            usuario_encontrado = usuario
            break

    if usuario_encontrado:
        contas.append({'agencia': agencia, 'numero_conta': conta_numero, 'usuario': usuario_encontrado})
        print(f"Conta corrente criada com sucesso para {usuario_encontrado['nome']}!")
    else:
        print("Erro! Usuário não encontrado com esse CPF.")

# Função para realizar o depósito
def depositar(saldo, valor, extrato):
    saldo += valor
    extrato += f"Depósito: R$ {valor:.2f}\n"
    return saldo, extrato

# Função para realizar o saque
def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato, numero_saques

# Função para exibir o extrato
def exibir_extrato(saldo, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

# Função principal para gerenciar o sistema bancário
def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []

    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [u] Criar usuário
    [c] Criar conta corrente
    [q] Sair
    => """
    
    while True:
        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            if valor > 0:
                saldo, extrato = depositar(saldo, valor, extrato)
            else:
                print("Operação falhou! O valor informado é inválido.")
        
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES)
        
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "u":
            nome = input("Informe o nome do usuário: ")
            data_nascimento = input("Informe a data de nascimento do usuário (DD/MM/AAAA): ")
            cpf = input("Informe o CPF do usuário: ")
            endereco = input("Informe o endereço do usuário (logradouro,nro-bairro-cidade/sigla do estado): ")
            criar_usuario(nome, data_nascimento, cpf, endereco, usuarios)
        
        elif opcao == "c":
            cpf = input("Informe o CPF do usuário para criar a conta corrente: ")
            criar_conta_corrente(cpf, contas, usuarios)
        
        elif opcao == "q":
            print("Saindo do sistema. Até logo!")
            break
        
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
    git init
    