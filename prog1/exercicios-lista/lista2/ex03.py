# Faça um programa que leia duas listas de inteiros, com 10 elementos cada. A seguir, calcule e imprima o lista-comum correspondente, isto é, uma lista de elementos cujos valores na primeira lista e estão na segunda.

def ler_lista():
    lista = []
    
    for i in range(10):
        valor = int(input(f'Digite o valor {i}°: '))
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

def lista_comum(lista1, lista2):
    resultado = []
    for i in range (len(lista1)):
        if esta_na_lista(lista1[i], lista2):
            resultado.append(lista1[i])
    return resultado

# Programa principal

lista_a = ler_lista('Lista A')
lista_b = ler_lista('Lista B')
comuns = lista_comum(lista_a, lista_b)

print('\n Lista-comum (elementos que estão em A que também estão em B)')
for i in range(len(comuns)):
    print(comuns[i])