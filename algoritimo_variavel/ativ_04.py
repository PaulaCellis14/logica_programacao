#1 - Solicitar o Salário Mensal: Use a função input() para pedir ao usuário que insira quanto ele ganha por mês. Converta a entrada do usuário de string para um número (float) para permitir cálculos.
#2 - Solicitar o Número de Horas Trabalhadas na Semana: Use a função input() para pedir ao usuário que insira o número de horas trabalhadas na semana. Converta a entrada do usuário de string para um número (float) para permitir cálculos.
#3 - Calcular o Total de Horas Trabalhadas no Mês: Multiplique o número de horas trabalhadas na semana por 4 para obter o total de horas trabalhadas no mês.
#4 - Calcular o Salário por Hora: Divida o salário mensal pelo total de horas trabalhadas no mês para obter o salário por hora.
#5 - Mostrar o Salário por Hora Calculado para o Usuário: Use a função print() para exibir o salário por hora calculado.

salario = float(input("Insira seu salário: R$"))
horas_trabalho = float(input("Insira as horas trabalhadas: "))

horas_mensais = horas_trabalho * 4
salario_hora = salario / horas_mensais

print(f"A sua hora de trabalho vale: {salario_hora}")
