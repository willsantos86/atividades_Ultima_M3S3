'''Uma loja de móveis está com dificuldades de calcular algumas condições de pagamento de seus móveis. 
Eles possuem algumas regras e o seu trabalho é implementar uma aplicação que faça os cálculos 
de acordo com as regras:
Regras
À vista em dinheiro, recebe 15% de desconto
À vista no cartão de crédito, recebe 10% de desconto
Em duas vezes, preço normal de etiqueta sem juros
Mais de duas vezes, preço normal de etiqueta mais juros de 10%

rograma deve ter uma variável com o valor de etiqueta do produto, 
uma variável com forma de pagamento e uma com o preço final após a aplicação de uma das regras.'''

valor = float(input('Digite o valor da compra: '))

dinheiro = valor * 0.85
cartão_a_vista = valor * 0.90
mais_vezes = valor * 1.10

print('''Formas de Pagamento (escolher o número conforme a opção desejada):
[1] = À vista
[2] = À vista no cartão
[3] = Dividir para 2x
[4] = Dividir para mais de 2x''')

print('=-'*20)

pagamento = int(input('===> Qual a forma de pagamento? '))

print('-'*40)

if pagamento == 1:
    print(f'O valor da compra com desconto de 15% foi de R$ {dinheiro:.2f}')
elif pagamento == 2:
    print(f'O valor da compra com desconto de 10% foi de R$ {cartão_a_vista:.2f}')
elif pagamento == 3:
    print(f'O valor da compra foi R$ {valor:.2f}')
else:
    print(f'O valor da compra com juros de 10% foi R$ {mais_vezes:.2f}')