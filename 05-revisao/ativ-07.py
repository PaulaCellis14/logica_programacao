#Algoritmo de Conversão de Tempo:
#Desenvolva um algoritmo que converta uma quantidade de segundos fornecida pelo usuário em horas, minutos e segundos.

# horas = total_segundos / 3600 (divisao inteira)
# resto = total_segundo % 3600
# minutos = resto / 60 (divisao inteira)
# segundos = resto % 60

total_segundos = int(input("Escreva quantos segundos quer converter para horas. "))

horas = total_segundos // 3600
resto = total_segundos % 3600
minutos = resto // 60
segundos = resto % 60

print(horas)
print(resto)
print(minutos)
print(segundos)

print(f"{total_segundos} convertidos em horas é: {horas}:{minutos}:{segundos}")