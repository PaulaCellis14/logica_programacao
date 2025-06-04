#Soma de Números Pares:
#Crie um programa que use um laço while para somar todos os números pares de 1 a 100 e exiba o resultado.

add = 0
counter = 1

while counter <= 100:
    counter += 1
    if counter % 2 == 0:
        add += counter
print(f"The sum all even numbers from 1 to 100 is: {add}")


