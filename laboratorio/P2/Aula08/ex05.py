# Escreva uma função na linguagem Python que receba uma matriz (lista de listas) de números e retorne os números máximo e mínimo desta matriz. Use estruturas de repetição.

def MaxMin(matriz):
    maior = matriz[0][0]
    menor = matriz[0][0]
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            if matriz[linha][coluna] > maior:
                maior = matriz[linha][coluna]
            elif matriz[linha][coluna] < menor:
                menor = matriz[linha][coluna]
    return maior, menor

def MaxMin(matriz):
    maior = matriz[0][0]
    menor = matriz[0][0]

    for linha in matriz:
        for valor in linha:
            if valor > maior:
                maior = valor
            elif valor < menor:
                menor = valor
    return maior, menor