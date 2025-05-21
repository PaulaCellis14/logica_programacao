#Verificação de Palavras em uma Frase:
#Peça ao usuário para inserir uma frase e uma palavra. Use in para verificar se a palavra está na frase.

# informações do tipo string solicitadas ao usuário através da função input
frase = str(input("Insira uma frase: "))
palavra = str(input("Insira uma palavra: "))

#função print se a palavra inserida esta prensente na frase inserida atrves do operador de associação in.
print(palavra in frase)