#Solicite as Notas do Usuário: Use a função input() para pedir ao usuário que insira cada uma das quatro notas bimestrais. Converta a entrada do usuário de string para um número (float) para permitir cálculos. Calcular a Média das Notas: Some as quatro notas e divida o resultado por quatro para obter a média. Mostrar a Média Calculada para o Usuário: Use a função print() para exibir a média das notas calculada.

#Aqui foi criada 4 variáveis nominadas de forma lógica, com a função input para que o usuário possa inserir os dado. Todas elas foram tipadas com float, para que o usuario possa inserir notas decimais.
nota_1 = float(input("Insira sua primeira nota: "))
nota_2 = float(input("Insira sua segunda nota: "))
nota_3 = float(input("Insira sua terceira nota: "))
nota_4 = float(input("Insira sua quarta nota: "))

#Aqui fizemo sum calculo para obter a media das notas. Criamos a variavel soma que soma as 4 notas inseridas pelo usuario. Criamos também a variavel media que divide o resultado de soma pela quantidade de notas pedidas (quatro). Essa variável resulta na media solicitada.
soma = nota_1 + nota_2 + nota_3 + nota_4
media = soma / 4

#Aqui usamos a função print para mostrar no terminal e dentro dessa função usamos a sintaxe "f-string" para juntarmos dentro da função strings e variáveis.
print(f"A média de suas notas é: {media}")