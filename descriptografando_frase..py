#Descriptografando frase.

frase_criptografada = 'HVWRX HPSROJDGR FRP R FXUVR GH SBWKRQ'
frase_descriptografada = ''
deslocamento = 3
for letra in frase_criptografada:
    if letra == ' ':
        frase_descriptografada += ' '
        continue

    codigo_letra = ord(letra)

    letra_descriptografada  = codigo_letra - deslocamento

    if letra_descriptografada < 65:
        letra_descriptografada += 26

    frase_descriptografada += chr(letra_descriptografada)
print(frase_descriptografada)


