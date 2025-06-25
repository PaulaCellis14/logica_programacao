#Cálculo de Juros Simples:
#Crie um programa que calcule o valor futuro de um investimento usando a fórmula de juros simples. Peça ao usuário para digitar o capital inicial, a taxa de juros e o tempo de aplicação.

# J = C * i * t

principal = float(input("Qual o capital inicial do investimento? "))
rate = float(input("Qual a taxa de juros do investimento? "))
time = float(input("Por quanto tempo irá fazer a aplicação? "))

interest = principal * rate * time
total_amount = principal + interest
print(f"O investimento renderá {interest}, e o valor final do montante sera {total_amount}.")