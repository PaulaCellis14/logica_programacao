#Contar números positivos e negativos
#Peça ao usuário para inserir 10 números. Use um laço for com condicionais para contar quantos são positivos e quantos são negativos. Pare o loop se o número 0 for inserido, usando break.

neg = 0
pos = 0

for i in range(10):
    n = int(input(f"Digite o número {i + 1: }"))

    if n == 0:
        print(f"O número {n} foi encontrado.")
        break
    elif n > 0:
        pos += 1
    else:
        neg += 1
print(f"{pos} são positivos.")
print(f"{neg} são negativos.")
