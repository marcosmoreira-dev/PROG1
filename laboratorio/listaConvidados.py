convidados = ['Maria', 'José', 'Alfredo']
print(convidados)
adicionar = input('Deseja adicionar mais um convidado? (S/N): ')


if adicionar == 'S':
    novoConvidado = input('Qual o nome do novo convidado? ')
    convidados.append(novoConvidado)
    print(convidados)

print('Um convidado cancelou a presença.')
convidadoCancelado = str(input('Insira o nome do convidado que cancelou a presença: '))
convidados.remove(convidadoCancelado)

convidados.sort()
print(convidados)
print(f'A quantidade de convidados é igual a {len(convidados)}')
