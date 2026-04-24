# Dada uma lista com elementos duplicados, como minha_lista = [1, 2, 3, 4, 4, 5, 1], escreva um programa que crie uma nova lista contendo apenas elementos únicos da lista original, sem repetições. A nova lista deve ser [1, 2, 3, 4, 5].

minhaLista = [1, 2, 3, 4, 4, 5, 1]
novaLista = []

for N in minhaLista:
    if N not in novaLista:
        novaLista.append(N)
print(novaLista)
