mensagem_criptografada = ['8', '5', '-1', '7', '6', '-1', '8', '4', '-1', '7', '3', '-1', '7', '7', '-1', '6', '5', '-1']
palavra = ''
codigo_letra = ''

for letra in mensagem_criptografada:

    if letra != '-1':
        codigo_letra += letra
    else:
        palavra += chr(int(codigo_letra))
        codigo_letra = ''
        

print(palavra)