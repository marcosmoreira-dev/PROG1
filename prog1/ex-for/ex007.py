# Escrever um programa que leia 5 valores, um de cada vez, e conta quantos destes valores são negativos.

contaNegativos = 0

for i in range(5):
    n = int(input('Digite um número inteiro: '))
    if n < 0: 
        contaNegativos = contaNegativos + 1
print(f'Negativos: {contaNegativos}')