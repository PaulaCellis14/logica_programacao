#Desenvolva um programa em Python para calcular a média de notas de alunos em uma disciplina. O programa deve solicitar ao usuário o número de alunos e, em seguida, para cada aluno, pedir o nome e três notas. Utilize um loop 'for' para iterar sobre os alunos e suas notas. Além disso, implemente uma estrutura condicional para verificar se cada aluno foi aprovado ou reprovado, considerando que a média mínima para aprovação é 7.0. Exiba o nome do aluno, suas notas, média e a indicação de aprovação ou reprovação. Ao final, exiba a média geral da turma.

num_alunos = int(input("Quantos alunos há na turma? ")) 
soma_medias = 0

for i in range(num_alunos):
    print(f"Aluno {i + 1}:")
    nome = input("Nome do aluno: ")
    notas = []
    soma = 0

    for j in range(3):
        nota = float(input(f"Digite a nota {j + 1}: "))
        notas.append(nota)
        soma += nota
    media = soma / 3
    soma_medias += media  # Acumula para média da turma

    if media >= 7.0:
        status = "Aprovado"
    else:
        status = "Reprovado"

    print(f"Nome: {nome}")
    print(f"Notas: {notas}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {status}")

media_turma = soma_medias / num_alunos
print(f"Média geral da turma: {media_turma:.2f}")