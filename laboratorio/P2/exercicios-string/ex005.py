# Faça um programa que peça ao usuário para digitar um nome ou expressão (ex: HyperText Markup Language). O programa deve gerar e exibir um acrônimo pegando a primeira letra de cada palavra em maiúscula (ex.: HTML)

alf_mais = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

texto = input('Digite um nome ou expressão: ')
acr = ''

for i in range(len(texto)):
    if texto[i] in alf_mais:
        acr = acr + texto[i]
print(acr)

## OU
# IF texto[i].isUpper()