#Soma de Números Pares:
#Crie um programa que use um laço while para somar todos os números pares de 1 a 100 e exiba o resultado.

contador = 1
pares = 0

while contador <= 100:
    contador += 1
    if contador % 2 == 0:
        pares += contador
    else:
        continue

print(f"A soma de todos os pares dos números entre 1 e 100 é {pares}.")
    