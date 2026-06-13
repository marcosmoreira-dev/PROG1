# Faça um programa em Python para ler, por meio de uma função, uma lista a de elementos inteiros e calcule e imprima o valor de S, sendo e calcule e imprimir quantos termos da série têm o numerador inferior ao denominador.

def ler_lista():
    lista = []
    n = int(input('Digite o número de elementos da lista: '))
    for i in range(n):
        valor = int(input(f'Digite o elemento {i}: '))
        lista.append(valor)
    return lista

def calcular_somatorio(lista):
    s = 0
    contador = 0
    
    for i in range(1, len(lista)):
        numerador = 1
        if lista[i] != 0:
            s += numerador / lista[i]
            if numerador < lista[i]:
                contador += 1
    return s, contador

lista = ler_lista()
soma, termos_menores = calcular_somatorio(lista)
print(soma)
print(termos_menores)
