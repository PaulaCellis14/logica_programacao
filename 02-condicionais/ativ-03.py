#Verificação de Maioridade e Habilitação:
#Crie um programa que peça a idade do usuário e se ele possui habilitação (sim ou não). Use operadores lógicos para verificar se ele é maior de idade (>= 18) e possui habilitação.

# informações do tipo inteiro e string solicitadas ao usuário através da função input
idade = int(input("Insira sua idade: "))
habilitado = str(input("Possui habilitação? (Sim ou Não)"))

#função print mostra se idade é maior ou igual que 18 e se a pessoa é habilitada.
print(idade >= 18 and habilitado == "Sim")