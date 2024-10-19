#Escreva um programa que o usuario inputa seu nome, seu salário e o % do seu bonus e é retornado uma saudação, o valor do bonus
#Salario*bonus + 1000

CONSTANTE_BONUS = 1000
#Input nome
nome = input('Insira seu nome ')

#input salario
salario = float(
    input(
        'Insira seu salario '
    )
)

#input percentual bonus
percentual_bonus = float(input('Percentual de bonus '))

#calculo do total recebido
calculo = (salario*percentual_bonus)+CONSTANTE_BONUS #substituindo o 1000 hard code por uma variável, melhor a longo prazo
remuneracao_total = salario+calculo
#print
print(f'Olá {nome}, o total de bonus recebido é de {calculo} e o total recebido no mês é de {remuneracao_total}')
#o f dentro do print permite printar textos e números/variáveis juntos, do contrário, retornaria um erro. Perceba que a sintaxe muda!!
