#Soma de Números Positivos:
#Escreva um programa que solicite números ao usuário até que ele digite um número negativo, somando apenas os números positivos inseridos.

numero = ""
soma = 0

num = int(input("Insira um número: "))

while numero > 0:
    numero = int(input("insira um número: "))
    if numero > 0:
        print("numero")
        soma += numero
    else:
        print("Número invalido.")

soma = 0
while num > 0:
    soma += num
    print(f"O número atual é {num} e soma dos número até aqui é {soma}.")
    num = int(input("Insira outro número: "))
if num < 0:
    print(f"O número {num} não pode ser aceito, portanto a soma dos números chegou à {soma}.")
