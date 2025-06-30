#Tabuada de um Número:
#Faça um programa que solicite um número ao usuário e use um laço for para exibir a tabuada desse número (de 1 a 10).

tabuada = int(input("Insira um número: "))

for i in range(1, 10 + 1):
    resultado = i * tabuada
    print(f"{i} * {tabuada} = {resultado}")