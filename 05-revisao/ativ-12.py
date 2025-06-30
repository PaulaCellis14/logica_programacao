#Sistema de Login:
#Desenvolva um programa que simule um sistema de login. O programa deve pedir o nome de usuário e a senha e verificar se correspondem a um usuário pré-cadastrado. Exiba mensagens apropriadas para login bem-sucedido ou falha.

login = str(input("Insira seu login: "))
senha = str(input("Insira sua senha: "))

if login == "admin" and senha == "1234":
    print("Bem vindo!")
else:
    print("Usuário ou senha inválidos. Tente novamente.")