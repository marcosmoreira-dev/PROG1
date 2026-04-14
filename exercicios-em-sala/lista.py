lista = []

for i in range(5):
    nome = input('Informe 5 nomes')
    lista.append(nome)

n = int(input('Giros: '))

for i in range(n):
    novaLista = lista[::-1]

print(f'Lista final {novaLista}')
