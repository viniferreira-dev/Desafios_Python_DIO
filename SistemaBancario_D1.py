saldo = 0
codigo = "0"
escolha_0_1 = ""
ext = []
numero_saque = 3

while codigo != "000":
    codigo = input(
    """
    # Escolha o código da operação:
    # Depósito | 001
    # Saque    | 002
    # Extrato  | 003
    # Sair     | 000
    Digite o código: 
    """)

    if codigo == "001":
        while escolha_0_1 != "0":
            dep = float(input("Insira o valor de depósito: "))
            if dep <= 0:
                print("Valor inválido! Tente novamente.")
                continue
            ext.append(dep)
            saldo += dep
            print('''Fazer novo depósito? 
                  Digite 1 para "Sim"
                  Digite 0 para "Não" ''')
            escolha_0_1 = str(input())
        escolha_0_1 = ""  

    elif codigo == "002":
        if numero_saque == 0:
            print("Número limite de saques diários atingidos! Voltando ao menu...")
            continue  

        while escolha_0_1 != "0":      
            saque = float(input("Insira o valor de saque: "))
            if saque <= 0:
                print("Valor inválido! Voltando ao menu...")
                break
            if (saldo - saque) < 0:
                print("Saldo insuficiente! Voltando ao menu...")
                break
            ext.append(saque * -1)
            saldo -= saque
            numero_saque -= 1
            if numero_saque == 0:
                print("Número limite de saques diários atingido! Voltando ao menu...")
                break
            print(f'''Fazer novo saque? (Restantes: {numero_saque}) 
                    Digite 1 para "Sim"
                    Digite 0 para "Não" ''')
            escolha_0_1 = str(input())
        escolha_0_1 = ""  

    elif codigo == "003":
        print("Extrato ------------------")
        for i in range(len(ext)):
            print(f"R$ {ext[i]:.2f}")
        print(f"Saldo: R$ {saldo:.2f}")

print("Obrigado por utilizar o nosso serviço!")
