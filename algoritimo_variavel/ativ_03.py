#1 - Solicitar as Notas do Usuário: Use a função input() para pedir ao usuário que insira cada uma das quatro notas bimestrais. Converta a entrada do usuário de string para um número (float) para permitir cálculos.
#2 - Calcular a Média das Notas: Some as quatro notas e divida o resultado por quatro para obter a média.
#3 - Mostrar a Média Calculada para o Usuário: Use a função print() para exibir a média das notas calculada.

nota_1 = float(input("Insira sua primeira nota: "))
nota_2 = float(input("Insira sua segunda nota: "))
nota_3 = float(input("Insira sua terceira nota: "))
nota_4 = float(input("Insira sua quarta nota: "))

soma = nota_1 + nota_2 + nota_3 + nota_4
media = soma / 4

print(f"A média de suas notas é: {media}")