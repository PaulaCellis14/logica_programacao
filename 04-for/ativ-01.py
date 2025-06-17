#Faça um programa que solicite um número ao usuário e use um laço for para exibir a tabuada desse número (de 1 a 10).

#1. Variável "number", tipo de dado inteiro, função input para entrada de dados.
#2. Variável "mult_table", lista de 1 à 10.
#3. Loop "for" para percorrer a lista, variável "numbers" para exibir no print cada item da lista, operador de associção "in" para verificar os itens dentro da lista mult_table.
#4. Função "print" para mostrar o resultado, f"" para colocar variaveis e strings juntas. Dentro de print está a variavel "numbers" mostrando cada item da lista, a variavel "number" mostrando o número inserido pelo usuário, e a expressão numbers * number, que exibe o resultado da multiplicação.

number = int(input("Insira um número: "))

mult_table = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numbers in mult_table:
    print(f"{numbers} * {number} = {numbers * number}")