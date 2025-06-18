#Contagem de Números Positivos e Negativos:
#Escreva um programa que solicite ao usuário 10 números e use um laço for com uma condicional para contar quantos são positivos e quantos são negativos.

#1. Pedi os números com a função input Como o tipo int aceita apenas 1 numero por vez, ao invés de solicitar 10 vezes a mesma coisa, deixei a entrada em formato de string para transforma-la depois em int.
#2. Criei uma variável que vai armazenar os numeros tranformados em inteiro. Como os dados estão em formato de string ".split()" vai separar cada numero a cada espaço, como se separasse as letras de uma palavra. map(int, ...) vai pegar cada item que foi separado e tranforma-los em inteiros. list vai pegar esses itens e coloca-los em formato de lista.
#3. Criei variáveis para armazenar temporareamente os itens e outras para somar a quantidade de positivos e negativos.
#4. O bloco for determina que para cada item da lista numbers, se o numero for igual ou maior que 0, esse item deve ser armazenado em positive_number, deve ser impresso a frase "O numero x é positivo." e será acrescido 1 à variavel positive_counter. Se o numero doir menor que 0, esse item será armazenado em negative_number, será impresso a frase "O numero x é negativo." e será acrescido 1 à variavel negative_counter.
#5. Ao final, o print vai mostrar a quantidade de numeros positivos e negativos que foram somados e armazenados em postive_counter e negative_counter.

user_numbers = input("Digite 10 números separdos por espaço: ")
numbers = list(map(int, user_numbers.split()))

positive_counter = 0
negative_counter = 0
positive_number = 0
negative_number = 0

for i in numbers:
    if i >= 0:
        positive_number = i
        print(f"O número {positive_number} é positivo.")
        positive_counter += 1
    else:
        negative_number = i
        print(f"O número {negative_number} é negativo.")
        negative_counter += 1
print(f"De todos os números inseridos, {positive_counter} são positivos e {negative_counter} são negativos.")