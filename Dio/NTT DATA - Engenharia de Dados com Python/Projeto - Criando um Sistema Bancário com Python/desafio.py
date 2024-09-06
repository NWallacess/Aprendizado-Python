# inicio

# Criando Variaveis

menu = """
1 - Depositar.
2 - Sacar.
3 - Visualizar Extrato.
4 - Sair.

"""
saldo = 0
deposito = 0
saque = 0
saque_realizados = 0
limite = 500
extrato = ""

while True:
    print(menu)
    opcao = int(input("Qual operação deseja realizar? "))

    # Deposito
    if opcao == 1:
        print("~"*10 + "Deposito" + "~"*10)
        while True:
            deposito = float(input("Quanto deseja depositar ? R$ "))
            if deposito <= 0:
                print("ERROO! Favor informar um valor positivo e diferente de 0.")
            else:
                saldo += deposito
                print(f"Deposito: R$ {deposito:.2f}.")
                extrato += f"Deposito: R$ {deposito:.2f}\n"
                break

    # Sacar
    elif opcao == 2:
        print("~"*10 + "Sacar" + "~"*10)
        while True:
            saque = float(input("Quanto deseja sacar? R$ "))

            if saque > limite:
                print("Operação falhou! O valor do saque excede o limite.")
                break

            elif saque_realizados >= 3:
                print("Operação falhou! Número máximo de saques excedido.")
                break

            elif saque > saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
                break

            elif saque > 0:
                saldo -= saque
                saque_realizados += 1
                print(f"Saque: R$ {saque:.2f}.")
                extrato += f"Saque: R$ {saque:.2f}.\n"
                break

            else:
                print("Operação falhou! O valor informado é inválido.")

    # Extrato:
    elif opcao == 3:
        print("~"*10 + "Extrato" + "~"*10)
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("~"*30)

    # Sair
    elif opcao == 4:
        break

    # Opção errado
    else:
        print("Operação falhou! Opção informado é inválido.")
