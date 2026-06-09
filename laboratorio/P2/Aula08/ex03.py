#Escreva um programa na linguagem Python que crie duas listas de números inteiros. Uma das listas deve conter apenas os múltiplos de 3 presentes no intervalo [ 1, 1000 ], a outra deve conter o restante dos números neste intervalo, ou seja, os que não são múltiplos de 3.

multiplos_3 = []
nao_multiplos_3 = []

for i in range(1, 1001):
    if i % 3 == 0:
        multiplos_3.append(i)
    else:
        nao_multiplos_3.append(i)

print(multiplos_3)
print(nao_multiplos_3)