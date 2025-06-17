#Entrada Válida:
#Crie um programa que solicite ao usuário um número entre 1 e 10. Continue pedindo até que o usuário forneça um valor válido.

entrada_valida = 3
tentativa = None

while tentativa != entrada_valida:
    tentativa = int(input("Qual o número de acesso: "))
    if tentativa == entrada_valida:
        print("Acesso concedido!")
        break
    else:
        print("Acesso negado. Tente novamente.")