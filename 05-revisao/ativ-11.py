#Verificar Signo:
#Escreva um programa que peça o dia e o mês de nascimento do usuário e informe o signo correspondente.

dia = int(input("Qual seu dia de nascimento? "))
mes = str(input("Qual seu mês de nascimento? "))

if dia >= 21 and mes == "março" or dia <= 19 and mes == "abril":
    print("Seu signo é aries.")
elif dia >= 20 and mes == "abril" or dia <= 20 and mes =="maio":
    print("Seu signo é touro.")
elif dia >= 21 and mes == "maio" or dia <= 20 and mes == "junho":
    print("Seu signo é gêmeos.")
elif dia >= 21 and mes == "junho" or dia <= 22 and mes == "julho":
    print("Seu signo é câncer.")
elif dia >= 23 and mes == "julho" or dia <= 22 and mes == "agosto":
    print("Seu signo é leão.")
elif dia >= 23 and mes == "agosto" or dia <= 22 and mes == "setembro":
    print("Seu signo é virgem.")
elif dia >= 23 and mes == "setembro" or dia <= 22 and mes == "outubro":
    print("Seu signo é libra.")
elif dia >= 23 and mes == "outubro" or dia <= 21 and mes == "novembro":
    print("Seu signo é escorpião.")
elif dia >= 22 and mes == "novembro" or dia <= 21 and mes == "dezembro":
    print("Seu signo é sagitário.")
elif dia >= 22 and mes == "dezembro" or dia <= 19 and mes == "janeiro":
    print("Seu signo é capricórnio.")
elif dia >= 20 and mes == "janeiro" or dia <= 18 and mes == "fevereiro":
    print("Seu signo é aquário.")
elif dia >= 19 and mes == "fevereiro" or dia <= 20 and mes == "março":
    print("Seu signo é peixes.")