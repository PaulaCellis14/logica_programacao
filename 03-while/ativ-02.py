#Soma de Números de 1 a 100:
#Escreva um programa que use um laço while para somar os números de 1 a 100 e exiba o resultado.

soma = 0
numero = 1

while numero <= 100:
    soma += numero
    numero += 1
print(f"A soma dos número de 1 à 100 é: {soma}")