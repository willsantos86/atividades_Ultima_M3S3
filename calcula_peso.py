'''Criei um programa que calcule o peso ideal de uma pessoa. Para isso utilize as fórmulas da tabela:'''

altura = float(input('Digite sua altura: '))
genero = str(input('Qual seu genero? [M/F]'))
masculino = (72.7 * altura) - 58
feminino = (62.1 * altura) - 44.7


if genero in 'Mm':
    print(f'Você é do sexo masculino, então seu peso ideal é: {masculino:.2f}Kg')
else:
    print(f'Você é do sexo feminino, então seu peso ideal é: {feminino:.2f}Kg')


#Sua aplicação deve identificar se a pessoa é Homem ou Mulher e então fazer o cálculo apropriado. 
# Deve ser impresso se a pessoa é homem ou mulher, juntamente com o peso ideal calculado.