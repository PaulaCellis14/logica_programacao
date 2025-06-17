#Desenvolva um jogo de adivinhação onde o programa escolhe um número aleatório entre 1 e 100. O usuário deve tentar adivinhar o número, e o programa deve fornecer dicas se o palpite está muito alto ou baixo.

guess = int(input("Adivinhe qual o número escolhido: "))

chosen_number = 27

while guess != chosen_number:
    if guess < chosen_number:
        guess = int(input("O número escolhido é um pouco mais alto. Escolha outro: "))
    elif guess > chosen_number:
        guess = int(input("O número escolhido é um pouco mais baixo. Escolha outro: "))
while guess == chosen_number:
    print("Você acertou!")
    break
    