#Contagem regressiva com verificação
#Faça um programa que use um laço while para fazer uma contagem regressiva de um número inserido pelo usuário até 0. Durante a contagem, exiba "Número par" para os números pares.

n = int(input("Digite um número: "))

while n >= 0:
    if n % 2 == 0:
        print(f"{n}: Número par")
        n -= 1
    else:
        print(n)
        n -= 1