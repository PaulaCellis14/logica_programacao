#Verificação de Palíndromo:
#Escreva um programa que solicite uma palavra ao usuário e use um laço while para verificar se a palavra é um palíndromo (lê-se da mesma forma de trás para frente).

palavra = str(input("Digite uma palavra: "))
palavra = palavra.lower()

i = 0
j = len(palavra) -1

palindromo = True

while i < j:
    if palavra[i] != palavra[j]:
        palindromo = False
        break
    else:
        i += 1
        j -= 1
    
if palindromo == False:
    print(f"A palavra {palavra.upper()} não é um palíndromo")
else:
    print(f"A palavra {palavra.upper()} é um palíndromo")



