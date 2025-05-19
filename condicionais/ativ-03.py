#Verificação de Maioridade e Habilitação:
#Crie um programa que peça a idade do usuário e se ele possui habilitação (sim ou não). Use operadores lógicos para verificar se ele é maior de idade (>= 18) e possui habilitação.

idade = int(input("Insira sua idade: "))
habilitado = str(input("Possui habilitação? (Sim ou Não)"))

print(idade >= 18 and habilitado == "Sim")