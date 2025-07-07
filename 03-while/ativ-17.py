#Fatorial de um número
#Desenvolva um programa que solicite um número ao usuário e use um laço while para calcular o fatorial desse número.

n = int(input("Digite um número: "))
numero = n
fatorial = 1

while numero >= 1:
    fatorial *= numero
    numero -= 1
print(f"O fatorial de {n} é {fatorial}.")
