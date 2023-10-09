menu = """

[d] depositar
[s] sacar
[e] extrato
[q] sair

=>"""

saldo=0
limite=500
extrato=""
ns=0
ls=3

while True:

    opcao=input(menu)

    if opcao =="d":
        print ("deposito")
        dp=float(input("digite o valor que deseja depositar:"))

        if dp>0:
            saldo+=dp
            extrato+= f"deposito de: R$ {dp:.2f}\n"

        else:
            print("opção invalida")    
        

    elif opcao=="s":
        print("saque")
        valor=float(input("digite o valor a ser sacado: "))

        exs=valor>saldo
        exl=valor>limite

        exsq=ns>=ls

        if exs:
            print("saldo insuficiente")

        elif exl:
            print("limite ultrapassado")

        elif exsq:
            print("limite de saques atingido")

        elif valor>0:
            saldo-=valor
            extrato+=f"saque: R$ {valor:.2f}\n"
            ns+=1    

        else:
            print("opção invalida")



    elif opcao=="e":
        print("não tiveram movimentações mesta conta" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}\n")

    elif opcao=="q":
        break            

    else:
        print("opção invalida")