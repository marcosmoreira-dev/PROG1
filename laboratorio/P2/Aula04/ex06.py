# 6) Escreva um programa que receba uma string e crie um dicionário onde as chaves são os caracteres e os valores são a quantidade de vezes que cada caractere aparece na string.

texto = input('Informe uma string: ')
frequencia = {}

for caractere in texto:
    if caractere == ' ':
        print('Caractere vazio')
    else:
        frequencia[caractere] == frequencia.get(caractere, 0) + 1
print(frequencia)