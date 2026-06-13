# Faça um programa que leia duas listas de inteiros, com 10 elementos cada. A seguir, calcule e imprima o lista-diferença correspondente, isto é, uma lista de elementos cujos valores na primeira lista e não estão na segunda.

def ler_lista(nome):
    lista = []
    print(f'Digite os 10 elementos da {nome}')
    for i in range(len(10)):
        valor = int(input(f'{nome} {i}: '))
        lista.append(valor)
    return lista

def esta_na_lista(valor, lista):
    i = 0
    achou = False

    while i < len(lista) and not achou:
        if lista[i] == valor:
            achou = True
        i += 1
        return achou
    
def lista_diferenca(lista1, lista2):
    resultado = []
    for i in range(len(lista1)):
        if not esta_na_lista(lista1[i], lista2):
            resultado.append(lista1[i])
    return resultado

lista_a = ler_lista('Lista A')
lista_b = ler_lista('Lista B')
diferenca = lista_diferenca(lista_a, lista_b)

print("\n Lista-diferença (elementos em A que não estão em B): ")
for i in range(len(diferenca)):
    print(diferenca[i])

