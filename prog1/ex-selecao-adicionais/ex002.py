# Corrigido

tipo = int(input('Digite o tipo de investimento (1/2): '))
valor = float(input('Digite o valor do investimento: '))

if tipo == 1:
    valorCorrigido = valor + (valor * 0.03)
    print('Tipo de Investimento: Poupança')
    print(f'Valor corrigido após 1 mês: {valorCorrigido}')
elif tipo == 2:
    valorCorrigido = valor + (valor * 0.04)
    print('Tipo de Investimento: Fundos de renda fixa')
    print(f'Valor corrigido após 1 mês: {valorCorrigido}')
else:
    print('Opção inválida!')



