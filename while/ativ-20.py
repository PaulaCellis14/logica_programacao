#Escreva um programa que solicite um número ao usuário e use um laço while para somar os dígitos do número até que a soma seja um único dígito.

#Usar (%) para pegar o ultimo numero
#Usar (//) para retirar o ultimo numero

number = int(input("Insira um número: "))

while number >= 10:
    sum = 0
    while number > 0:
        sum += number % 10
        number = number // 10
    number = sum
print(sum)
