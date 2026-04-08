# Escreva um programa que leia 3 números e imprima o menor deles (suponha números diferentes).

N1 = float(input('Digite o primeiro valor: '))
N2 = float(input('Digite o segundo valor: '))
N3 = float(input('Digite o terceiro valor: '))

if (N1 < N2) and (N1 < N3):
    menor = N1
elif N2 < N3:
    menor = N2
else:
    menor = N3

print(f'O menor número é o {menor}')