#Verificar Par ou Ímpar:
#Crie um programa que peça ao usuário um número e use a estrutura condicional if para verificar se ele é par ou ímpar.

num = int(input("Insira um número: "))

if num % 2 == 0:
    print(f"O número {num} é par.")
else:
    print(f"O número {num} é ímpar.")