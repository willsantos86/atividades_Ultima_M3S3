'''Um nutricionista está precisando de uma ajuda para calcular o IMC de seus pacientes. 
Para calcular o IMC ele passou a seguinte fórmula: IMC = peso / ( altura )². 
Crie um programa que faça o cálculo do IMC de uma pessoa (ele deve ser impresso na tela) 
e classifique o IMC dessa pessoa de acordo com a tabela (também deverá ser impresso):'''

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura**2)

print(f'O IMC é: {imc:.1f}')

if imc < 18.5:
    print(f'ATENÇÃO!!! Você está abaixo do peso!')
elif 18.5 >= imc < 25:
    print(f'PARABÉNS!!! Você está com peso normal!')
elif 25 >= imc < 30:
    print(f'ATENÇÃO!!! Você está acima do peso!')
else:
    print(f'ATENÇÃO!!! Você está OBESO!!')
