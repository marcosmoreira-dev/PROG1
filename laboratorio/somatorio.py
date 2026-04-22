# Somatório de n números: Vamos criar um programa 
# que some n números inteiros e imprima o resultado da soma

soma = 0
n = int(input("Digite um número inteiro: "))

while n != -1:
    soma = soma + n
    n = int(input('Digite outro número inteiro: '))

print(f'O resultado da soma é {soma}')
