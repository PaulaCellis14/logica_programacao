#Faça um programa que use um laço while para exibir os primeiros 20 termos da sequência de Fibonacci.

temp_term = 0
previous_term = 0
current_term = 1
counter = 1

while counter <= 20:
    print(previous_term)
    temp_term = previous_term
    previous_term = current_term
    current_term = temp_term + previous_term
    counter += 1

    

