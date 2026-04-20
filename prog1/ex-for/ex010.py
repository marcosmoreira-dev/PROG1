# Escreva um programa que leia 5 valores inteiros, um de cada vez, e calcule a média aritmética dos números lidos.

total = 0

for i in range(5):
    valor = int(input('Digite um valor: '))
    total = total + valor

media = total / 5
print(f'A média é igual a: {media}')