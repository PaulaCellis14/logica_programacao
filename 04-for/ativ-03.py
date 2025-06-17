#Escreva um programa que solicite uma palavra ao usuário e use um laço for para exibir cada caractere da palavra em uma linha separada.

#1. Variável "word" para armazenar a entrada de dados. Tipo string para aceitar apenas texto. Função input para permitir a entrada de dados.
#2. Loop for, para repetir a iteração. Variável "letter" para armazenar as iterações. Operador de associação in para verificar o conteúdo da variável "word."
#3. Função print para mostrar cada iteração.

word = str(input("Insira uma palavra: "))

for letter in word:
    print(letter)