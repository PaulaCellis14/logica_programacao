#Desenvolva um programa que solicite as notas dos alunos até que o usuário digite -1. Calcule e exiba a média das notas inseridas.

nota = float(input("Insira suas notas: "))

soma = 0
quantidade = 0

while nota != -1:
    soma += nota
    quantidade += 1
    print(f"Nota inserida: {nota}. Somatório {soma:.2f}. Quantidade de notas inseridas {quantidade}.")
    nota = float(input('Insira outra nota: '))
if nota == -1:
    media = soma / quantidade
    print(f"Cálculo encerrado. A média das suas notas é: {media:.2f}")