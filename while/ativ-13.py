#jogo de adivinhação onde dois jogadores tem 3 tentativas para adivinhar um número secreto.

secret_number = 7
total_attempts = 3
attempts_player1 = 0
attempts_player2 = 0

while attempts_player1 < total_attempts and attempts_player2 < total_attempts:
    guess1 = int(input("Player 1, guess the secret number."))
    attempts_player1 += 1
    if guess1 == secret_number:
        print("Player 1 is the winner of the game!")
        break
    else: 
        print("You're wrong!")

    guess2 = int(input("Player 2, guess the sectre_number."))
    attempts_player2 += 1
    if guess2 == secret_number:
        print("Player 2 is the winner of the game!")
        break
    else:
        print("You're wrong.")
else:
    print("There isn't winners on this game!")


