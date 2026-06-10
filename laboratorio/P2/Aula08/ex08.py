numero = int(input('Digite um número para começar a Conjectura de Collatz: '))

print(numero)

while numero != 1:
    if numero % 2 == 0:
        numero = numero // 2
    else:
        numero = (3 * numero) + 1

    print(numero)
print('Fim!')