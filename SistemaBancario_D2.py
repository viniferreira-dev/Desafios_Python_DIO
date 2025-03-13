'''
Em geral, a parte mais importante do código é a validação de login e sua utilização para manter a interação entre o usuário 
escolhido e as outras operações do programa.

Na função validar_login, há um loop que percorre todos os usuários e utiliza uma condicional para verificar se a conta e a 
senha pertencem a um dos usuários da lista. Se pertencerem, a função retorna o usuário correspondente (um dicionário); 
caso contrário, retorna None.

Dentro da função menu_inicial, definimos uma variável chamada usuario_logado, que representa a saída de validar_login. 
Quando o login é realizado com sucesso, passamos esse usuario_logado como argumento para a função menu, que, 
por sua vez, repassa o mesmo argumento para as operações de depósito, saque e extrato.

Vale lembrar que saldo, número de saques (nmr_saque) e a lista de extrato (extrato) fazem parte do dicionário do usuário. 
Diferentemente do projeto anterior, como esses objetos estão dentro de um dicionário, aplicamos as operações diretamente 
sobre o usuário logado.

Por fim, é importante destacar que o programa roda indefinidamente, pois a única opção existente para sair é retornar ao menu inicial.
'''


usuarios = [] 

# Função para inserir dados do usuário
def cadastro():
    print("======= Cadastro ========")
    nome = str(input("Nome: "))
    idade = int(input("Idade: ")) 
    genero = str(input("Genêro: "))
    email = str(input("E-mail: "))
    numero_conta = str(input("Número da Conta: ")) 
    senha_conta = str(input("Senha: "))
    return {"nome": nome, "idade": idade, "genero": genero, "email": email, 
            "numero": numero_conta, "senha": senha_conta, "saldo": 0.0, "nmr_saque": 3, "extrato": []}

# Função para validar o login
def validar_login(numero_conta, senha_conta):
    for usuario in usuarios:
        if usuario["numero"] == numero_conta and usuario["senha"] == senha_conta:
            return usuario
    return None

# Função para cadastrar o usuário no banco de dados
def cadastrar_usuario(cadastro_func):
    usuario = cadastro_func()  # Essa 'cadastro_func' é a 'cadastro' quando chamamos as duas  
    usuarios.append(usuario)  
    print("Usuário cadastrado com sucesso!")

# Função para fazer login
def login():
    print("======= Login ========")
    numero_conta = str(input("Número da Conta: ")) 
    senha_conta = str(input("Senha: "))
    return numero_conta, senha_conta

# Função do menu bancário
def menu(usuario_logado):
    while True:  # Loop que roda para sempre, só sai se eu seleciono 'sair'
        codigo = str(input(
            """
            # Escolha o código da operação:
            # Depósito | 001
            # Saque    | 002
            # Extrato  | 003
            # Sair     | 000
            Digite o código: 
            """))
        
        if codigo == "001":
            depositar(usuario_logado)  
        elif codigo == "002":
            sacar(usuario_logado)  
        elif codigo == "003":
            extrato(usuario_logado)  
        elif codigo == "000":
            print("Saindo...")
            return menu_inicial()  # Chama o menu inicial novamente
        else:
            print("Opção inválida! Tente novamente...")

# Função para depósito
def depositar(usuario_logado):
    dep = float(input("Insira o valor de depósito: "))
    if dep <= 0:
        print("Valor inválido! Tente novamente.")
        return depositar(usuario_logado)
    else:
        usuario_logado["extrato"].append(dep)
        usuario_logado["saldo"] += dep
        print(f"Depósito de R$ {dep:.2f} realizado com sucesso!")
        return menu(usuario_logado)

# Função para saque
def sacar(usuario_logado):
    if usuario_logado["nmr_saque"] == 0:
        print("Número limite de saques diários atingidos! Voltando ao menu...")
        return menu(usuario_logado)
    else:
        saque = float(input("Insira o valor de saque: "))
        if saque <= 0:
            print("Valor inválido! Voltando ao menu...")
            return menu(usuario_logado)
        if (usuario_logado["saldo"] - saque) < 0:
            print("Saldo insuficiente! Voltando ao menu...")
            return menu(usuario_logado)
        usuario_logado["extrato"].append(saque * -1)
        usuario_logado["saldo"] -= saque
        usuario_logado["nmr_saque"] -= 1
        print(f"Saque de R$ {saque:.2f} realizado com sucesso!")
        return menu(usuario_logado)

# Função para exibir o extrato
def extrato(usuario_logado):
    print("Extrato ------------------")
    for valor in usuario_logado["extrato"]:
        print(f"R$ {valor:.2f}")
    print(f"Saldo: R$ {usuario_logado['saldo']:.2f}")
    print("Selecione qualquer tecla para voltar ao menu.")
    return menu(usuario_logado)

# Função para o menu inicial
def menu_inicial():
    opcao = input('''Escolha uma das opções:
                  (1) Cadastrar Novo Usuário
                  (2) Fazer Login''')
    if opcao == "1":
        cadastrar_usuario(cadastro)  # Passa a função(dict) `cadastro` como argumento
        return menu_inicial()
    elif opcao == "2":
        numero_conta, senha_conta = login()  
        usuario_logado = validar_login(numero_conta, senha_conta)  
        while not usuario_logado:  # Enquanto o login for inválido, solicita novamente
            print("Senha ou Usuário inválidos. Tente novamente...")
            numero_conta, senha_conta = login()
            usuario_logado = validar_login(numero_conta, senha_conta)
        print("Login bem-sucedido!")
        menu(usuario_logado)  # Passa o usuário logado para o menu bancário
    else: 
        print("Opção inválida, voltando para o menu inicial...")
        return menu_inicial()

menu_inicial()

