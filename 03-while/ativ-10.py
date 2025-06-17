#Escreva um programa que use um laço while para somar números consecutivos começando de 1 e termine quando a soma atingir ou ultrapassar 50.

soma = 0
contador = 1

while soma <= 50:
    print(soma)
    soma += contador
    contador += 1
    if soma >= 50:
        break