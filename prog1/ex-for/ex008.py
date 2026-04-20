# Escrever um programa que leia 5 valores, um de cada vez, e conta quantos deles estão em cada um dos intervalos: [0, 25], (25, 50], (50, ∞).

conta25 = 0
conta50 = 0
contaMaior50 = 0

for i in range(5):
    numero = int(input('Digite um valor inteiro: '))
    
    if numero >= 0 and numero <= 25:
        conta25 = conta25 + 1
    elif numero > 25 and numero <= 50:
        conta50 = conta50 + 1
    elif numero > 50:
        contaMaior50 = contaMaior50 + 1
    else:
        print('Número não é maior que 0.')
print(f'Números entre 0 e 25: {conta25}')
print(f'Números entre 25 e 50: {conta50}')
print(f'Números maiores que 50: {contaMaior50}')