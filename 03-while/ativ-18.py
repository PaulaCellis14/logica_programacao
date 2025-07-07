#Números Pares em um Intervalo:
#Crie um programa que solicite dois números ao usuário, representando um intervalo. Use um laço while para exibir todos os números pares dentro desse intervalo.

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
pares = 0

while n1 < n2:
    if n1 % 2 == 0:
        pares = n1
        print(pares)
        n1 += 1
    else:
        n1 += 1