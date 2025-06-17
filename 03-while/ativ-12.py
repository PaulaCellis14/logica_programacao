#Desenvolva um programa que peça ao usuário para digitar uma senha e continue pedindo até que a senha correta (previamente definida) seja inserida.

senha_correta = "paula"
tentativa = None

while tentative != senha_correta:
    tentativa = input("Insira sua senha: ")
    if tentativa == senha_correta:
        print("Bem vindo!")
        break
    else:
        print("Senha incorreta.  tente novamente.")