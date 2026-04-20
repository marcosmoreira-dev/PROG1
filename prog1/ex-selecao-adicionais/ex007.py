# Não corrigido

codigo = int(input('Digite o código do cargo: '))
salario = float(input('Digite o salário atual: '))

if codigo == 1:
    print('Cargo: Escriturário')
    aumento = 0.5
if codigo == 2:
    print('Cargo: Secretário')
    aumento = 0.35
if codigo == 3:
    print('Cargo: Caixa')
    aumento = 0.2
if codigo == 4:
    print('Cargo: Gerente')
    aumento = 0.1
if codigo == 5:
    print('Cargo: Diretor')
    aumento = 'Não tem aumento'

print(f'Valor do aumento: {aumento}')

novoSalario = salario + (salario * aumento)

print(f'O novo salário é igual a: {novoSalario}')