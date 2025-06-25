#Verificando a Média do Aluno:
#Crie um algoritmo que peça quatro notas de um aluno, calcule a média e exiba se o aluno foi aprovado ou reprovado (média >= 6).
#media = soma dos valores / numero de valores

grade_1 = float(input("Nos informe a nota do primeiro bimestre: ")) 
grade_2 = float(input("Nos informe a nota do segundo bimestre: "))
grade_3 = float(input("Nos informe a nota do terceiro bimestre: ")) 
grade_4 = float(input("Nos informe a nota do quarto bimestre: "))

sum = grade_1 + grade_2 + grade_3 + grade_4
average = sum / 4

if average >= 6:
    print(f"Sua média é {average:.2f}, portanto você foi aprovado.")
else:
    print(f"Sua média é {average:.2f}, portanto você foi reprovado.")






