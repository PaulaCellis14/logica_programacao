#Contagem de vogais em uma Palavra
#Crie um programa que solicite uma palavra ao usuário e use um laço for com uma condicional para contar quantas vogais (a, e, i, o, u) a palavra contém.

#1. Solicitado a entrada de dados em forma de string.
#2. Variável "sum" para armazenar o total de vogais da palavra.
#3. Para cada letra na palavra inserida, se a letra estiver contida em "aeiou", mostre A letra x é uma vogal, incremente 1 a varivael soma.
#4. No final mostramos o tatal de vogais na palavra inserida.

word = str(input("Digite uma palavra: "))
sum = 0

for caractere in word:
    if caractere.lower() in "aeiou":
        print(f"A letra '{caractere}' é uma vogal.")
        sum += 1
print(f"O total de vogais na palavra {word} é {sum}.")