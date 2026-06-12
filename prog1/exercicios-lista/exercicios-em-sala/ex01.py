def obterLista(lista, quantidade):
    for i in range(quantidade):
        valor = int(input('Digite o valor: '))
        lista.append(valor)
    return lista

def obterPosMenor(lista):
    menor = lista[0]
    posMenor = 0

    for i in range(len(lista)):
        if lista[i] < menor:
            posMenor = i
            menor = lista[i]
    return posMenor

def obterPosMenorAPartirDe(lista, pos):
    menor = lista[pos]
    posMenor = pos

    for i in range(pos + 1, len(lista)):
        if lista[i] < menor:
            posMenor = i
            menor = lista[i]

    return posMenor

def permutar(p1, p2, lista):
    aux = lista[p1]
    lista[p1] = lista[p2]
    lista[p2] = aux

def ordenar(lista):
    for posInicial in range(len(lista)):
        posMenor = obterPosMenor(lista, posInicial)
        if posMenor != posInicial:
            permutar(posMenor, posInicial, lista)