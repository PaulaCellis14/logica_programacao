#Algoritmo de Conversão de Temperatura:
#Crie um algoritmo que converta uma temperatura de Celsius para Fahrenheit. Solicite ao usuário a temperatura em Celsius e exiba o resultado em Fahrenheit.

#f = (c x 9/5) + 32

celsius = float(input("Qual é a temperuta da sua cidade? "))
fahrenheit = celsius * 9 / 5 + 32

print(f"A temperatura {celsius}ºC convertida para fahrenheit é: {fahrenheit}ºF.")