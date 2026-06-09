# Escreva uma função em Python que receba uma lista de números e retorne o maior número presente no lista.
def maior(lista):
    maior = lista[0]
    for valor in lista:
        if valor > maior:
            maior = valor
    return maior

def menor(lista): 
    menor = lista[0]
    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]
    return menor