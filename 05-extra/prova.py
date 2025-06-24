# Quantidade de alunos solicitada e variável que vai armazenar a soma das médias de todos os alunos.
alunos = int(input("Qual a quantidade de alunos na turma? ")) 
soma_total = 0 

#Bloco for que itera sobre a quantidade de alunos inserida pedindo nome e com variáveis para armazenar as informaçoes.
for i in range(alunos):
    nome = str(input("Digite o nome do aluno: "))
    nota_aluno = []
    soma = 0
    
    #Bloco for que itera sobre a quantidade de notas que vão ser inseridas. Variáveis para armazenar ou somar as informações.
    for i in range(3):
        nota = float(input(f"Insira a nota {i + 1} de {nome}: "))
        nota_aluno.append(nota)
        soma += nota
    media_aluno = soma / 3
    soma_total += media_aluno
        
    #bloco pra mostrar informações.
    print(f"Relatório do aluno {nome}.")
    print(f"Suas três notas foram, repectivamente: {nota_aluno}.")
    print(f"A sua média é: {media_aluno:.2f}")
    
    #condicionais para verificar a aprovação e reprovação dos alunos
    if media_aluno >= 7.0:
        print(f"O aluno {nome} foi aprovado!")
    else:
        print(f"O aluno {nome} foi reprovado.")

#Cálculo da média total e print para mostrar a média.
media_total = soma_total / alunos
print(f"A media geral da turma é: {media_total:.2f}")