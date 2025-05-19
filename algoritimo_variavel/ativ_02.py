#Crie um programa que peça ao usuário para digitar:
#1.Seu nome;
#2.Sua idade;
#3.Sua altura;
#4.Em seguida, imprima esses valores e seus respectivos tipos.

nome = str(input("Insira seu nome: "))
idade = int(input("Insira sua idade: "))
altura = float(input("Insira sua altura: "))

print(nome, type(nome))
print(idade, type(idade))
print(altura, type(altura))