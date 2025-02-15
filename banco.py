# 3 funções - extrato, saque e depósito
import time

saldo = 0

transacoes = []

def saque():
    global saldo, transacoes
    s = float(input("digite o valor a ser sacado do seu saldo:\n>>> "))
    time.sleep(1.5)
    if(s>saldo):
        print("você não possui saldo o suficiente")
    else:
        saldo -= s
        transacoes.append(f"Valor do saque: R${s:.2f}")
        print(f"Seu novo saldo eh de: R${saldo:.2f}")

def deposito():
    global saldo, transacoes
    d = float(input("Digite o valor a ser depositado na sua conta:\n>>> "))
    time.sleep(1.5)
    saldo += d
    transacoes.append(f"Valor do deposito: R${d:.2f}")
    print(f"Seu novo saldo eh de: R${saldo:.2f}")

def extrato():
    global saldo, transacoes
    time.sleep(1.5)
    print("\n--- Extrato Bancário ---")
    print(f"---Proprietario: {nome}---")
    if not transacoes:  
        print("Nenhuma transação realizada ate o momento.")
    else:
        for transacao in transacoes:  
            print(transacao)
    print(f"Saldo atual: R${saldo:.2f}\n")

nome = input("digite o nome do proprietario da conta:\n>>> ")
time.sleep(1.5)

while(1):
    op = int(input(f"Bem vindo(a) {nome}, qual sera a operaçao realizada?\n1-saque\n2-deposito\n3-extrato\n>>> "))

    if(op == 1):
        saque()
    elif(op==2):
        deposito()
    elif(op==3):
        extrato()
    else:
        print("opção inválida")