# Peça ao usuário um número inteiro N. Escreva um programa que gere e imprima os N primeiros termos da sequência de Fibonacci. A sequência começa com 0 e 1, e cada termo subsequente é a soma dos dois anteriores (Ex.: 0, 1, 1, 2, 3, 5, 8, ...)

fibo = [0, 1]
n = int(input('Digite um número: '))

if n > 1:
    for i in range(0, n+1):
        fibo.append(fibo[i+1] + fibo[i])
        print(fibo)
else:
    print('Digite um número válido')