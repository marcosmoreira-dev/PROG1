# Rescreva o programa abaixo que exclui um elemento da lista em uma determinada posição e obter o valor excluído, mas utilizando uma função.
# lista = [1, 2, 3, 4]
# pos = 2
# elementoRetirado = 0
# temp = []
# for i in range(len(lista)):
#     if i != pos:
#         temp.append(lista[i])
#     else:
#         elementoRetirado = lista[i]
# lista = temp
# print(lista)
# print(elementoRetirado)

lista = [1, 2, 3, 4]
pos = 2

def excluiValor(lista, pos):
    temp = []
    elementoRetirado = 0

    for i in range(len(lista)):
        if i != pos:
            temp.append(lista[i])
        else:
            elementoRetirado = lista[i]
    return temp, elementoRetirado

novaLista, retirado = excluiValor(lista, pos)
print(novaLista)
print(retirado)