#Você está desenvolvendo um programa em Python para calcular a soma dos números pares dentro de um intervalo determinado pelo usuário. O programa deve solicitar ao usuário que insira dois números inteiros, representando o início e o fim do intervalo (inclusive). Utilize um loop 'for' para iterar sobre todos os números no intervalo e somar apenas os números pares. Implemente a estrutura 'else' para exibir uma mensagem indicando que não há números pares no intervalo, caso seja o caso. Ao final, exiba a soma dos números pares encontrados.

first_number = int(input("Insira o primeiro número: ")) #Primeiro número inserido pelo usuário.
second_number = int(input("Insira o segundo número: ")) #Segundo número inserido pelo usuário.

sum = 0 #Variável onde a soma dos números pares será armazenda.

for i in range(first_number, second_number + 1): #loop for. Range começando pelo 1º número e terminando no 2º. Foi preciso usar a expressão "+ 1" para o 2º número ser incluído no intervalo.
    if i % 2 == 0: #Se o número do intervalo for par:
        sum += i #Soma com o valor de sum e é atribuido a sum.
print(f"A soma de todos os números pares do intervalo é: {sum}") #Mostra no terminal o resultado.


