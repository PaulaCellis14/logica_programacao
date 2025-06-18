#Soma de números pares
#Escreva um programa que use um laço for para somar todos os números pares de 1 a 50 e exiba o resultado final.

sum = 0

for i in range(1, 51):
    if i % 2 == 0:
        sum += i
print(f"A soma dos números pares entre 1 e 50 é: {sum}")
        