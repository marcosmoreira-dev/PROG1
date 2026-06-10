# Escreva uma função na linguagem Python que receba uma lista de pares de comprimentos de catetos de triângulos retângulos e retorne uma lista com os comprimentos de cada respectiva hipotenusa.

def calculaHipotenusa(lista):
    listaHipotenusa = []
    for i in range(len(lista)):
        h = ((lista[i][0] ** 2) + (lista[i][1] ** 2)) ** (1/2)
        listaHipotenusa.append(h)

    return listaHipotenusa

# OU 
def calculaHipotenusa2(lista):
    listaHipotenusa = []
    for cateto1, cateto2 in lista:
        h = (cateto1 ** 2) + (cateto2 ** 2) ** 0.5
        listaHipotenusa.append(h)
    return listaHipotenusa


catetos = [ (3, 4), (5, 12), (6, 8)]
hipotenusas = calculaHipotenusa(catetos)
print(hipotenusas)

