#Verificar Status de Taxa de Desconto:
#Crie um programa que peça ao usuário o preço original de um produto e a quantidade comprada. Use if para verificar se a quantidade é maior que 10 para aplicar um desconto de 10% sobre o total.

preco_original = float(input("Insira o preço original do produto: "))
quantidade = int(input("Isnira a quantidade comprada: "))

desconto = preco_original *= 0.10

if quantidade > 10:
    print(f"O valor total da compra é de R${desconto * 10}.")
else:
    print(F"O valor totao da compra é de R${preco_original * 10}.")