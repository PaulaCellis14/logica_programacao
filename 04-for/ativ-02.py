#Crie um programa que use um laço for para somar todos os números de 1 a 100 e exiba o resultado.

#1. Variável "sum = 0" para somar com cada iteração e armazenar o resultado.
#2. Loop "for" para realizar a repetição, variavel "number" para armazenar cada iteração, range(1, 101) para fazer a soma do start (1) até o stop -1 (100).
#3. Incremento "sum += number" - o valor de cada iteração é somado com o valor que está um sum e o resultado é atribuído a sum.
#4. Função "print(sum)" para mostrar cada alteração em sum.
#5. Se identarmos print no mesmo nível de for, irá aparecer somente o resultado final.
sum = 0

for number in range(1, 101)
    sum += number
    print(sum)
