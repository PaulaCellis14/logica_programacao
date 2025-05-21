#Verificar Par ou Ímpar e Positivo ou Negativo:
#Escreva um programa que peça um número e use if para verificar se ele é par ou ímpar e também se é positivo ou negativo.

num = int(input("Insira um número: "))

if num % 2 == 0 and num > 0:
    print(f"O número {num} é par e positivo.")
elif num % 2 != 0 and num > 0:
    print(f"O número {num} é ímpar e positivo.")
elif num % 2 == 0 and num < 0:
    print(f"O número {num} é par e negativo.") 
else:
    print(F"O número {num} é ímpar e negativo.")