# 3 funções - extrato, saque e depósito
import time

def saque():
    saldo = 0
    s = float(input("digite o valor a ser sacado do seu saldo:\n>>> "))
    time.sleep(1.5)
    if(s>saldo):
        print("você não possui saldo o suficiente")
    else:
        print(f"Seu novo saldo eh de: R${s-saldo}")

def deposito():
    saldo = 0
    d = float(input("digite o valor a ser depositado na sua conta:\n>>> "))
    time.sleep(1.5)
    print(f"Seu novo saldo eh de: R${d+saldo}")

nome = input("digite o nome do proprietario da conta:\n>>> ")

op = int(input(f"Bem vindo(a) {nome}, qual sera a operaçao realizada?\n1-saque\n2-deposito\n3-extrato\n>>> "))

if(op == 1):
    saque()
elif(op==2):
    deposito()