#Tabuada com Condicional:
#Faça um programa que solicite um número ao usuário e use um laço while para exibir a tabuada desse número (de 1 a 10), mas apenas para os resultados que forem múltiplos de 3.

numero = int(input("Insira um número: "))

multiplicador = 1
while multiplicador <= 10:
    resultado = numero * multiplicador
    if resultado % 3 == 0:
        print(f"{numero} * {multiplicador} = {resultado}")
    multiplicador += 1

