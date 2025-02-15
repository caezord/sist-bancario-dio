# 3 funções - extrato, saque e depósito
import time

saldo = 0
saques = 0
transacoes = []

def saque():
    global saldo, transacoes, saques
    if(saques > 3):
        print("\nVoce atingiu a quantidade maxima de saques diarios")
        return

    s = float(input("\ndigite o valor a ser sacado do seu saldo:\n>>> "))
    time.sleep(1.5)
    if(s>saldo):
        print("você não possui saldo o suficiente")
    else:
        if(s>500.0):
            print("\no valor máximo para fazer saques é de R$500.00")
        else:
            saques += 1
            saldo -= s
            transacoes.append(f"\nValor do saque: R${s:.2f}")
            print(f"Seu novo saldo é de: R${saldo:.2f}")

def deposito():
    global saldo, transacoes
    d = float(input("\nDigite o valor a ser depositado na sua conta:\n>>> "))
    time.sleep(1.5)
    saldo += d
    transacoes.append(f"\nValor do deposito: R${d:.2f}")
    print(f"Seu novo saldo é de: R${saldo:.2f}")

def extrato():
    global saldo, transacoes
    time.sleep(1.5)
    print("\n--- Extrato Bancário ---")
    print(f"---Proprietario: {nome}---")
    if not transacoes:  
        print("\nNenhuma transação realizada ate o momento.")
    else:
        for transacao in transacoes:  
            print(transacao)
    print(f"\nSaldo atual: R${saldo:.2f}\n")

nome = input("digite o nome do proprietario da conta:\n>>> ")
time.sleep(1.5)

while(1):
    op = int(input(f"\nBem vindo(a) {nome}, qual sera a operaçao realizada?\n1-saque\n2-deposito\n3-extrato\n>>> "))

    if(op == 1):
        saque()
    elif(op==2):
        deposito()
    elif(op==3):
        extrato()
    else:
        print("opção inválida")