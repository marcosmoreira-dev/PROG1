# Dada a lista numeros = [12, -5, 23, 4, 18, 9, 27, 10, -1], escreva um programa que crie uma nova lista contendo apenas números que são maiores que 10. Ao final, imprima a nova lista.

numeros = [12, -5, 23, 4, 18, 9, 27, 10, -1]
lista = []

for i in range(len(numeros)):
    if numeros[i] > 10:
        lista.append(numeros[i])
print(lista)

# Ou usando IN

numbers = [12, -5, 23, 4, 18, 9, 27, 10, -1]
nova_lista = []

for numero in numbers:
    if numero > 10:
        nova_lista.append(numero)
print(nova_lista)
