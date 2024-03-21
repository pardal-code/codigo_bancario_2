def menu():

    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova Conta
    [c] Contas
    [nu] Novo Usuario
    [q] Sair

    => """

    return input(menu)

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: \tR$ {valor:.2f}\n"
        print("\n === Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou: O valor informado é inválido @@@")

    return saldo, extrato

def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > limite_saques

    if excedeu_limite:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente @@@")
    
    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t R$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso!")
        extrato += f"Saldo Total:\t R$ {saldo:.2f}\n"

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido @@@")

    return saldo, extrato

def exibir_extrato(saldo, extrato):
    print("\n================= EXTRATO =================")
    print("Não foram realizados movimentações." if not extrato else extrato)
    print("=============================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento: ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado: )")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("==== Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\n@@@ Usuário não foi encotrado, fluxo de criação de conta encerrado")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta["agencia"]}
            C/C:\t{conta["numero_conta"]}
            Titular:\t{conta["usuario"]["nome"]}
        """
        print("=" * 100)
        print(linha)

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        cpf = input("Por favor, insira o seu CPF (somente números) ou 'q' para sair: ")

        if cpf == "q":
            break

        usuario = filtrar_usuario(cpf, usuarios)

        if not usuario:
            print("CPF não encontrado, por favor, proceda com o cadastro.")
            criar_usuario(usuarios)

        print("\n=== Bem-vindo ao banco! ===")
        print("[d] Depositar")
        print("[s] Sacar")
        print("[e] Extrato")
        print("[c] Contas")
        print("[q] Sair")

        opcao = input("Por favor, selecione a operação desejada: ")

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato)
        
        elif opcao == "c":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
