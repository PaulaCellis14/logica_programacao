#Cálculo de média em notas
#Escreva um programa que solicite 5 notas de alunos. Use um laço for para somar as notas e uma condicional para exibir a média e a classificação ("Aprovado" para média >= 6, "Reprovado" para média < 6).

student = input("Digite suas notas de Matemática, Português, Ciências, História e Geografia, respectivamente: ")
grades = list(map(float, student.split()))

grade_sum = 0
grade_average = 0

for i in grades:
    grade_sum += i
    grade_average += grade_sum / 5
    
if grade_average >= 6:
    print("Você foi aprovado.")
else:
    print("Você foi reprovado.")
