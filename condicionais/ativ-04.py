#Verificação de Notas Aprovadas:
#Escreva um programa que peça duas notas de um aluno. Use operadores lógicos para verificar se as duas notas são maiores ou iguais a 6.

nota_mat = float(input("Insira sua nota de matemática: "))
nota_his = float(input("Insira sua nota de história: "))

print(nota_mat >= 6 and nota_his >= 6)