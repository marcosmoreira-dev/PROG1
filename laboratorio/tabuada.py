# Tabuada da Multiplicação: vamos criar um programa que pede um 
# número ao usuário e exibe sua tabuada de 1 a 10

n = int(input('Digite um número para ver a sua tabuada: '))

for i in range(1, 11, 1):
    total = n * i
    print(f'{n} x {i} = {total}')
