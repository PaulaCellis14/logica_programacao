#Verificar Classificação de IMC:
#Crie um programa que calcule o Índice de Massa Corporal (IMC) e use if para classificar o resultado em "Abaixo do peso", "Peso normal", "Sobrepeso" e "Obesidade".

#calculo imc = peso / altura ** 2

peso = float(input("Insira seu peso: "))
altura = float(input("insira sua altura: "))

imc = peso / altura ** 2

if imc <= 18.5:
    print("Você está abaixo do peso.")
elif imc <= 24.99:
    print("Você esta como o peso normal.")
elif imc <= 29.99:
    print("Você está com sobrepeso.")
else:
    print("Você está com obesidade.")