#1 - Solicitar o Nome do Usuário: Use a função input() para pedir ao usuário que insira seu nome.
#2 - Solicitar a Idade do Usuário: Use a função input() para pedir ao usuário que insira sua idade. Converta a entrada do usuário de string para um número (int).
#3 - Solicitar a Cidade Natal do Usuário: Use a função input() para pedir ao usuário que insira sua cidade natal.
#4 - Formatar e Exibir a Mensagem com f-string: Use uma f-string para formatar a mensagem com as informações fornecidas pelo usuário e exiba a mensagem usando a função print().

#Aqui foi criada 3 variáveis nominadas de forma lógica, com a função input para que o usuário possa inserir os dado. duas foram tipadas como str, para o usuário inserir caracteres e a outra foi tipada como int, sendo permitido somente numeros interos como dado.
nome = str(input("Insira seu nome: "))
idade = int(input("Insira sua idade: "))
naturalidade = str(input("Insira sua cidade natal: "))

#Aqui usamos a função print para mostrar o resultado no terminal e dentro dessa função usamos a sintaxe "f-string" para juntarmos dentro da função strings e variáveis.
print(f"Meu nome é {nome}, minha idade é {idade} e nasci em {naturalidade}.")