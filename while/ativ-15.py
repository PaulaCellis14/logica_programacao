#Números Ímpares de 1 a 50:
#Escreva um programa que use um laço while para exibir todos os números ímpares de 1 a 50.

contador = 0

while contador < 50:
    contador += 1
    if contador % 2 != 0:
        print(contador)
