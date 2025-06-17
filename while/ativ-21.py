#Crie um programa que solicite um número ao usuário e use um laço while para gerar e exibir a sequência de Collatz até chegar ao número 1.

number = int(input("Insira um número: "))

while number > 1:
    if number % 2 == 0:
        number /= 2
    else:
        number = number * 3 + 1
    print(number)