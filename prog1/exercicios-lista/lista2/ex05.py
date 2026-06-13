# Escreva um programa em Python que leia uma lista e posteriormente faça a rotação de seus elementos. Imprima a lista antes e depois da rotação.

def ler_lista():
    lista = []
    n = int(input('Digite o número de elementos da lista: '))
    for i in range(n):
        valor = int(input(f'Elemento {i}: '))
        lista.append(valor)
    return lista

def rotacionar_lista(lista):
    n = len(lista)
    i = 0
    while i < n // 2:
        temp = lista[i]
        lista[i] = lista[n - 1 - i]
        lista[n - 1 - i] = temp
        i += 1

# Programa principal

lista = ler_lista()
print('\nLista original: ')
for i in range(len(lista)):
    print(lista[i])

rotacionar_lista(lista)

print('\nLista após rotação:')
for i in range(len(lista)):
    print(lista[i])