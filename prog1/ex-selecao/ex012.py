# n1 = float(input('Digite o primeiro valor: '))
# n2 = float(input('Digite o segundo valor: '))
# n3 = float(input('Digite o terceiro valor: '))

# if (n1 == n2) and (n1 == n3):
#    print('Os números são todos iguais')
# elif (n1 >= n2) and (n1 >= n3):
#    maior = n1
# elif n2 >= n3:
#     maior = n2
# else:
#    maior = n3

# print('MAIOR = ', maior)

numero1 = float(input('Número 1: '))
numero2 = float(input('Número 1: '))
numero3 = float(input('Número 1: '))

maior = numero1

if numero2 > maior:
    maior = numero2
elif numero3 > maior:
    maior =  numero3

print('O maior número é: ', maior)

if numero1 == numero2 or numero1 == numero3 or numero2 == numero3:
    print('Os seguintes números são iguais: ')
    if numero1 == numero2:
        print('Número 1 e Número 2: ', numero1)
    if numero1 == numero3:
        print('Número 1 e Número 3: ', numero1)
    if numero2 == numero3:
        print('Número 2 e Número 3: ', numero2)
else:
    print('Não há números iguais entre os fornecidos')
