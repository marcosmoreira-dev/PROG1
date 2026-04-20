# Escreva um programa que leia 5 valores inteiros, um de cada vez e calcule a soma deles.

soma = 0

for i in range(5):
    valor = int(input('Digite um valor: '))
    soma = soma + valor

print('A soma é igual a: ', soma)