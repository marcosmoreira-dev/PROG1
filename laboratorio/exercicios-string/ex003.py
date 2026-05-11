# Faça um programa que verifique se uma palavra digitada pelo usuário é um palídromo. Um palíndromo é uma palavra que se lê da mesma forma de trás para frente

palavra = input('Digite uma palavra: ')
inv = palavra[::-1]

if palavra == inv:
    print('A palavra é um palíndromo')
else:
    print('A palavra digitada não é um palídromo')