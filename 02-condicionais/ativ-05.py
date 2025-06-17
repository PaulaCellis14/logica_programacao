#Desconto em Preço:
#Peça ao usuário para inserir o preço de um produto e, em seguida, use o operador de atribuição -= para aplicar um desconto de 5%.

# informações do tipo float solicitadas ao usuário através da função input
preco = float(input("Informe o preço do produto"))

#Operação que atribui à preço um desconto de 5%.
preco -= preco * 0.05

#função print mostra o valor do produto já com o desconto.
#f"string" usada para juntarmos strings e variaveis na mesma função.
print(f"R${preco:.2f}")