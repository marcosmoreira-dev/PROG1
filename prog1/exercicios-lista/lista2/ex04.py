# Faça um programa em Python para ler, por meio de uma função, uma lista A de elementos inteiros, escreva uma função que gere (crie uma nova) uma lista B cujos componentes são os fatoriais dos respectivos componentes de A. Imprima as listas A e B.

def ler_lista(nome):
    lista = []
    n = int(input(f'Digite o número de elemendos da {nome}: '))
    for i in range(n):
        valor = int(input(f'{nome}[{i}]: '))
        lista.append(valor)
    return lista

def fatorial(n):
    resultado = 1
    i = 1
    while i <= n:
        resultado *= i
        i += 1
    return resultado

def gerar_lista_fatoriais(lista_a):
    lista_b = []
    for i in range(len(lista_a)):
        fat = fatorial(lista_a[i])
        lista_b.append(fat)
    return lista_b

lista_a = ler_lista('Lista A')
lista_b = gerar_lista_fatoriais(lista_a)

print('\n Lista A:')
for i in range(len(lista_a)):
    print(lista_a[i])

print('\n Lista B (fatoriais de A):')
for i in range(len(lista_b)):
    print(lista_b[i])