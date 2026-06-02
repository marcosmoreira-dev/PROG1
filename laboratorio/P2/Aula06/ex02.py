# Crie uma função chamada media_ponderada que receba uma lista de tuplas, onde cada tupla contém (nota, peso). A função deve calcular e retornar a média ponderada.
# ● Exemplo de entrada: [(8.0, 2), (9.0, 3), (7.0, 5)]

listaTuplas = [(8.0, 2),
               (9.0, 3),
               (7.0, 5)]

def media_ponderada(lista):
    soma = 0
    peso = 0 
    for i in range(len(lista)):
        soma += lista[i][0] * lista[i][1]
        peso += lista[i][1]
    media = soma / peso
    return media

print(media_ponderada(listaTuplas))
    


