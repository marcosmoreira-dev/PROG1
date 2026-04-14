listaC = []
listaA = ['a', 'c', 'e']
listaB = ['b', 'd', 'f']
tam = len(listaA)

for i in range(tam):
    #Adiciona indice 0 da lista A
    listaC.append(listaA[i])
    #Adciona indice 0 da lista B
    listaC.append(listaB[i])

print(listaC)
