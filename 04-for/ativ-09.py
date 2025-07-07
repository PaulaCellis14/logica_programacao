#Verificar Números Pares e Impares com Interrupção:
#Crie um programa que use um laço for para contar de 1 a 20. Use condicionais para identificar números pares e ímpares. Pare o loop ao encontrar o número 15, usando break.

for i in range(1, 20 + 1):
    if i == 15:
        print(f"Número {i} encontrado.")
        break
    elif i % 2 == 0:
        print(f"{i}: Número par.")
    else:
        print(f"{i}: Número ímpar.")