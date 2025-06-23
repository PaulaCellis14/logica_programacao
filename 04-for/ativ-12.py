#Soma de Números com Desconto:
#Peça ao usuário para inserir 5 preços de produtos. Use um laço for para calcular o total. Aplique um desconto de 10% se o total ultrapassar 100 e interrompa o loop com break.

total = 0

for i in range(5):
    price = float(input(f"Insira O valor do produto {i + 1} R$"))
    total += price

    if total > 100:
        print("Total ultrapassou 100. Aplicando desconte de 10%.")
        total *= 0.9
        break

print(f"Total a pagar R${total.:2f}")
