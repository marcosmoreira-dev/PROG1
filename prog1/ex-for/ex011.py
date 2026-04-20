# Escreva um programa que leia 5 valores inteiros, um de cada vez. Encontrar e escrever o maior valor lido.

maior = int(input('Digite um valor inteiro: '))

for i in range(4): 
    valor = int(input('Digite um valor inteiro: '))
    if valor > maior:
        maior = valor

print(f'O maior valor é: {maior}')