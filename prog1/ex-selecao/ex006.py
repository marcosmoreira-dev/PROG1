# Faça um programa que leia um número inteiro maior 0. Caso o número seja par e menor que 10, escreva ‘Número par e menor que Dez’, caso o número digitado seja ímpar e menor que 10 escreva ‘Número Ímpar menor que Dez’, caso contrário escreva ‘Número fora do Intervalo’.

valor = int(input('Digite um valor: '))

if valor > 0:
    if (valor % 2 == 0) and (valor < 10):
        print('Número par e menor que 10')
    elif (valor % 2 != 0 and valor < 10):
        print('Número ímpar e menor que 10')
    else:
        print('Número fora do intervalo')
else:
    print('Número fora do intervalo')