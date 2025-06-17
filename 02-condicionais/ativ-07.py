#Verificação de Caracteres em uma String:
#Crie um programa que peça ao usuário uma frase e um caractere. Use o operador de associação in para verificar se o caractere está presente na frase

# informações do tipo string solicitadas ao usuário através da função input
frase = str(input("Escreva um frase: "))
caractere = str(input("Escreva um caractere: "))

#função print mostra se o caractere está presente na frase usando o operador de associação in.
print(caractere in frase)

