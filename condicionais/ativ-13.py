#Sistema de Login Simples:
#Desenvolva um programa que peça ao usuário um nome de usuário e uma senha e use if para verificar se são iguais a "admin" e "1234", respectivamente.

usuario = str(input("Insira seu nome de usuário: "))
senha = int(input("Insira sua senha: "))

if usuario == "admin" and senha == 1234:
    print("Bem vindo!")
elif usuario != "admin" and senha == 1234:
    print("Usuário inválido. Tente novamente.")
elif usuario == "admin" and senha != 1234:
    print("Senha inváida. Tente novamente.")
else:
    print("Usuário e senha inválidos. Tente novamente.")