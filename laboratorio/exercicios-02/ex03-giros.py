lista = []

for i in range(5):
    num = int(input('Informe um número: '))
    lista.append(num)

n = int(input('Giros: '))

for i in range(n):
    ultimo = lista.pop()
    lista.insert(0, ultimo)

print(f'Lista final {lista}')
