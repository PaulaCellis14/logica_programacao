#Contagem até o Número Inserido:
#Crie um programa que solicite um número ao usuário e use um laço while para contar de 1 até o número inserido, exibindo apenas os números ímpares.

numero = int(input("Insira um número: "))

numero_impar = 0
while numero_impar <= numero:
    numero_impar += 1
    if numero_impar % 2 != 0:
        print(numero_impar)