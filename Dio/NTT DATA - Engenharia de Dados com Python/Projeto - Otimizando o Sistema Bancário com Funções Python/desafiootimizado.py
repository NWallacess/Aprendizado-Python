# inicio

#Declaração de variaveis
usuarios=[{"Usuario":"00","Nome":"Nicholas Wallace","Data de Nasc":"04/12/1999","CPF":"012.391.242-12","Endereço":"Marechal Floriano 99, Centro - RJ"}]
contasCorrente = [{"Usuario":"01","CPF":"012.391.242-12", "Nº da Conta":"40028922","Agencia":"0001"}]

#Definições das rotinas

def menu():
    menuu = """
=============Menu=============
1 - Depositar.
2 - Sacar.
3 - Visualizar Extrato.
4 - Nova conta
5 - Listar contas
6 - Novo usuarios
9 - Sair.
==============================
=> Qual opção deseja? 
"""
    escolha = int(input(f"{menuu}"))
    return escolha

def sacar(*,saldo_fun:float,valor_fun:float, extrato_fun:str,limite_fun:float=500,num_saque:int=0,limiteSaque_fun:int=3):
    while True:
        if valor_fun > limite_fun:
            print("Operação falhou! O valor do saque excede o limite.")
            valor_fun = float(input("Quanto deseja sacar? R$ "))

        elif num_saque >= limiteSaque_fun:
            print("Operação falhou! Número máximo de saques excedido.")
            break

        elif valor_fun > saldo_fun:
            print("Operação falhou! Você não tem saldo suficiente.")
            break

        elif valor_fun > 0:
            saldo_fun -= valor_fun
            print(f"Saque: R$ {valor_fun:.2f}.")
            extrato_fun += f"Saque: R$ {valor_fun:.2f}.\n"
            break

        else:
            print("Operação falhou! O valor informado é inválido.")
            valor_fun = float(input("Quanto deseja sacar? R$ "))

    return saldo_fun, extrato_fun

def depositar(saldo_fun:float, deposito_fun:float, extrato_fun):
    while True:
        if deposito_fun == 0:
            deposito_fun = float(input("ERROOO! Informe um valor valido por gentileza.\nQual operação deseja realizar? R$"))
        else:
            saldo_fun += deposito_fun
            print(f"Deposito: R$ {deposito_fun:.2f}.")
            extrato_fun += f"Deposito: R$ {deposito_fun:.2f}\n"
            break
    return saldo_fun, extrato_fun

def extrato_bancario(saldo_fun, extrato_fun="Saldo: R$ "):
        print("Não foram realizadas movimentações." if not extrato_fun else extrato_fun)
        print(f"Saldo: R$ {saldo_fun:.2f}")

def criarUsuario(nome:str, data_de_nasc:str, cpf:str, end:str):
    global usuarios
    for l in range(len(usuarios)):
        if usuarios[l]["CPF"] == cpf:
            print("Usuario ja existente")
        else:
            novo_usuario = dict()
            novo_usuario["Usuario"] = f"0{len(usuarios) + 1}"
            novo_usuario["Nome"] = nome
            novo_usuario["Data de Nasc"] =data_de_nasc
            novo_usuario["CPF"] = cpf
            novo_usuario["Endereço"]=end
            usuarios.append(novo_usuario)
    
def criar_ContaCorrente(usuario_FUN:dict, conta:str, agencia:str="0001"):
    while True:
        global contasCorrente
        if usuario_FUN["CPF"] in contasCorrente:
            print("Esse usuario já tem conta nessa agencia!")
            opcaoCc = input("Deseja informar outra agencia? [S/N] ").upper()[1]
            if opcaoCc == 'S':
                agencia = input("Qual é o numero da agencia? ")
            else:
                return
        else:
            global usuarios
            nova_conta = dict()
            nova_conta ["Usuario"] = f"0 {len(usuarios)}"
            nova_conta ["Nº da Conta"] = conta
            nova_conta["CPF"] = usuario_FUN ["CPF"]
            nova_conta ["Agencia"] = agencia
            #{"Usuario":"01", "Nº da Conta":"40028922","Agencia":"0001"}
            break
    
    return nova_conta

def main():
    saldo = 0
    LIMITE = 500
    saques_realizados= 0
    valor = 0
    LIMITE_SAQUES = 3
    extrato =''

    while True:
        opcao = menu()
        
        if opcao == 2:
            print("=============SACAR=============")
            valor = float(input("Qual valor deseja sacar? R$ "))
            saldo , extrato = sacar(saldo_fun=saldo,
                                    valor_fun=valor,
                                    extrato_fun=extrato,
                                    limite_fun=LIMITE,
                                    num_saque=saques_realizados,
                                    limiteSaque_fun=LIMITE_SAQUES) 
            saques_realizados+= 1
        
        elif opcao == 1 :
            print("=============DEPOSITO=============")
            valor = float(input("Qual valor deseja depositar? R$ "))
            saldo , extrato = depositar(saldo_fun=saldo,deposito_fun=valor,extrato_fun=extrato)
        
        elif opcao == 3:
            print("=============EXTRATO=============")
            extrato_bancario(saldo_fun=saldo,extrato_fun=extrato)
        
        elif opcao == 4:
            print("==== CRIAR CONTA CORRENTE =====")
            addUsuario = usuarios[int(input("Qual usuario desseja cadastrar? "))]
            numcontanova = len(usuarios) +1
            novoUsuario = criar_ContaCorrente(usuario_FUN=addUsuario,conta=numcontanova)
            contasCorrente.append(novoUsuario)

        elif opcao == 5:
            print("===== LISTAR CONTAS ======")
            print(contasCorrente)

        elif opcao == 6:
            print("===== CRIAR USUARIO ======")
            addNome = input("Informe o nome do novo usuario: ")
            addDataDeNasc = input("Informe o data de nascimento do novo usuario: ")
            addEnd = input("Informe o endereço do novo usuario: ")
            addCPF= input("Informe o CPF do novo usuario: ")
            criarUsuario(nome=addNome,cpf=addCPF,end=addEnd,data_de_nasc=addDataDeNasc)
            print("Usuario criado!!!")
            print(usuarios[-1])

        elif opcao == 7:
            print(usuarios)
        
        elif opcao ==9:
            print("===== ENCERRANDO ======")
            break
            
        else:
            print("EERROOO!!! Por gentileza informar uma opção validada. ")

#Programa
main()