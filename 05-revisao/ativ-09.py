#Categoria de Idade:
#Desenvolva um programa que peça a idade do usuário e informe se ele é criança, adolescente, adulto ou idoso.

idade = int(input("Qual a sua idade? "))

if idade <= 2:
    print("Você ainda é um bebê!")
elif idade <= 5:
    print("Você esstá na primeira infância.")
elif idade <= 12:
    print("Você é criança.")
elif idade <= 17:
    print("Você está na adolescência.")
elif idade <= 24:
    print("Você é jovem.")
elif idade <= 59:
    print("Você está na fase adulta.")
else:
    print("Você é idoso.")
