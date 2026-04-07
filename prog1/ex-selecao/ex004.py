altura = float('Digite a sua altura: ')
sexo = input('Qual o seu sexo: (M/F): ')

if sexo == 'M':
    pesoIdeal = (62.1 * altura) - 44.7
    print(pesoIdeal)
elif sexo == 'F':
    pesoIdeal = (72.7 * altura) - 58
    print(pesoIdeal)
else:
    print('Você colocou um sexo que não existe')
