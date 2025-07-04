#Faça aqui um programa que, com base no tamanho de um objeto celeste em quilômetros, identifica se ele é um asteroide, um planeta ou uma estrela. O usuário deverá informar o tamanho do objeto celeste em quilômetros. O programa determinará: Asteroide: menor que 1.000 km. Planeta: entre 1.000 km e 140.000 km. Estrela: maior que 140.000 km. O programa exibirá a classificação correspondente.

objeto_celeste = float(input("Qual é o tamanho do objeto celeste avistado: "))

if objeto_celeste < 1000:
    print(f"O tamanho do objeto celeste corresponde à {objeto_celeste} km. Portando sua classificação é Asteróide.")
elif objeto_celeste <= 140000:
    print(f"O tamanho do objeto celeste corresponde à {objeto_celeste} km. Portando sua classificação é Planeta.")
else:
    print(f"O tamanho do objeto celeste corresponde à {objeto_celeste} km. Portando sua classificação é Estrela.")
