#Solicite o Salário Mensal: Use a função input() para pedir ao usuário que insira quanto ele ganha por mês. Converta a entrada do usuário de string para um número (float) para permitir cálculos Solicite o Número de Horas Trabalhadas na Semana: Use a função input() para pedir ao usuário que insira o número de horas trabalhadas na semana. Converta a entrada do usuário de string para um número (float) para permitir cálculos. Calcule o Total de Horas Trabalhadas no Mês: Multiplique o número de horas trabalhadas na semana por 4 para obter o total de horas trabalhadas no mês. Calcule o Salário por Hora: Divida o salário mensal pelo total de horas trabalhadas no mês para obter o salário por hora. Mostre o Salário por Hora Calculado para o Usuário: Use a função print() para exibir o salário por hora calculado.

#Aqui foi criada 2 variáveis nominadas de forma lógica, com a função input para que o usuário possa inserir os dado. as duas foram tipadas com float, para que o usuario possa inserir numeros decimais.
salario = float(input("Insira seu salário: R$"))
horas_trabalho = float(input("Insira as horas trabalhadas: "))

#Aqui, criamos a variavel "horas_mensais". Pegamos o dado inserido pelo usuário na variavel "horas_trabalho" e multiplicamos com o operador aritmetico "*" por quatro, que e a quantidade de semanas do mês. Criamos depois a variável "salario_hora", onde pegamos o dado da variavel "salário" e dividimos com o operador aritmerio "/", pelo resultado da variavel "horas_trabalhadas".
horas_mensais = horas_trabalho * 4
salario_hora = salario / horas_mensais

#Aqui usamos a função print para mostrar o resultado no terminal e dentro dessa função usamos a sintaxe "f-string" para juntarmos dentro da função strings e variáveis.
print(f"A sua hora de trabalho vale: {salario_hora}")
