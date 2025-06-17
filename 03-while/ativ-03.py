#Tabuada de um Número:
#Faça um programa que solicite um número ao usuário e use um laço while para exibir a tabuada desse número (de 1 a 10).

tabuada = int(input("Insira um número: "))

multiplicador = 0
numero = 1

while numero <= 10:
    multiplicador = tabuada * numero
    print(f"{tabuada} * {numero} = {multiplicador}")
    numero += 1
