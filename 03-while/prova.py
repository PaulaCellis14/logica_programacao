#Você está criando um programa em Python para simular um jogo simples de adivinhação. por exemplo, 7, que o jogador deve adivinhar. O jogador terá até 3 tentativas para acertar o número. Implemente o jogo utilizando um loop while para permitir que o jogador faça múltiplas tentativas até acertar ou atingir o limite de tentativas. Utilize a estrutura else para exibir uma mensagem de encorajamento caso o jogador acerte e uma mensagem de consolo caso as 3 tentativas se esgotem sem sucesso.

#1: Criei duas variáveis. 
    #1.1: "chosen_number" para armazenar o número secreto
    #1.2: "attempts" que é onde eu vou armazenar e atualizar o número de tentativas do jogador.

#2: Criei o loop while determinando que enquanto as tentativas do jogador forem menor ou igual a 3, o usuário vai continuar inserindo algum numero. 
    #2.1: Pra isso, foi criado a variavel "guess", foi definido que o tipo da variável é "int" para que seja aceito somente números inteiros e a função "input" que permite a entrada de dados.

#3: Criei uma estrutura de condicionais. 
    #3.1: Primeiro com o "if" determinando que se as tentativas chegarem a 3, o usuário será informado de que não há mais tentativas. 
    #3.2: Foi usado o break para que o loop se incerre, caso contrário, seria solicitado novamente um outro número, porque o loop funciona até 3 tentativas.
    
    #3.3: Segui com o "elif" determinando que se o número inserido pelo usuário for igual ao número secreto, ele receberá a mensagem dizendo que acertou.
    #3.4: O código se encerra pelo break, pelo mesmo motivo de antes.
    
    #3.5: Segui com o "else" determinando que se o numero não for 7, será solicitado outro. 
    #3.: Foi determinado que a variavel "attempts" terá um incremento de 1. Então cada vez que o usuário inserir um número, será adicionado 1 ao valor da váriável.

secret_number = 7
attempts = 1 

while attempts <= 3:
    guess = int(input("Adivinhe o número: "))

    if attempts == 3:
        print("Suas tentativas acabaram. Volte em alguns instantes.")
        break
    elif guess == secret_number:
        print("Parabéns. Você acertou.")
        break
    else:
        print("Você errou. Tente novamente.")
        attempts += 1

