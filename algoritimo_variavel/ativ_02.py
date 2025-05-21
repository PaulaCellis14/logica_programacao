#Crie um programa que peça ao usuário para digitar: Seu nome; Sua idade; Sua altura e em seguida, 
imprima esses valores e seus respectivos tipos.

#Aqui foi criada 3 variáveis nominadas de forma lógica, com a função input para que o usuário possa inserir os dado. A variável nome foi tipada como string, pois vai receber apenas caracteres, a variável idade foi tipada como int pois vai receber apenas numeros inteiros e a variavel altura foi tipada como float, pois pode receber numeros decimais.
nome = str(input("Insira seu nome: "))
idade = int(input("Insira sua idade: "))
altura = float(input("Insira sua altura: "))

#Aqui usamos a função print para mostrar os resultados no terminal e dentro de print usamos a função type para ser retornado qual o tipo de dado das variaveis.
print(nome, type(nome))
print(idade, type(idade))
print(altura, type(altura))