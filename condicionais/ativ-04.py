#Verificação de Notas Aprovadas:
#Escreva um programa que peça duas notas de um aluno. Use operadores lógicos para verificar se as duas notas são maiores ou iguais a 6.

# informações do tipo float solicitadas ao usuário através da função input
nota_mat = float(input("Insira sua nota de matemática: "))
nota_his = float(input("Insira sua nota de história: "))

#função print mostra se ambas as notas inseridas são maiores ou iguais a 6.
print(nota_mat >= 6 and nota_his >= 6)