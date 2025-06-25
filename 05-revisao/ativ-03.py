#Cálculo de IMC: 
#Crie um programa que calcule o Índice de Massa Corporal (IMC). Peça ao usuário para digitar seu peso e altura, armazene em variáveis e calcule o IMC.

#IMC = peso / altura
#BMI = weight / height

weight = float(input("Informe o seu peso para o cálculo: "))
height = float(input("Informe a sua altura para o cálculo: "))

bmi = weight / height ** 2
print(f"O seu índice de massa corporal é: {bmi:.2f}")