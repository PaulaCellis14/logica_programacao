#Algoritmo de Cálculo de Desconto:
#Desenvolva um algoritmo que calcule o preço de um produto após aplicar um desconto. Solicite o preço original e o percentual de desconto.
# valor do desconto = preço original * percentual do desconto/ 100

price = float(input("Qual o preço do produto que comprou? "))
discount = float(input("Qual o disconto oferecido? "))

discount_amount = price * discount / 100
final_price = price - discount_amount
print(f"O valor original do produto é R${price}. O desconto aplicado foi de {discount}%.")
print(f"O valor do desconto é R${discount_amount}, portanto o preço final é R${final_price}.")