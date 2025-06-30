#Classificação de Notas:
#Crie um programa que solicite uma nota de 0 a 100 e informe o conceito (A, B, C, D, F) com base na nota.

nota = float(input("Qual é a sua nota? "))

if nota >= 90:
    print("Sua classificação é: A")
elif nota >= 80:
    print("Sua classificação é: B")
elif nota >= 70:
    print("Sua classificação é: C")
elif nota >= 60:
    print("Sua classificação é: D")
elif nota >= 50:
    print("Sua classificação é: E")
else:
    print("Sua classificação é: F")