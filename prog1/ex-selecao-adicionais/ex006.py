# Não corrigido

print('Menu de Opções')
print('1. Somar dois números')
print('2. Raiz Quadrada de um número')
opcao = int(input('Digite a opção desejada: '))

if opcao == 1:
    print('Opção 1 selecionada')
    n1 = int(input('Digite o primeiro valor: '))
    n2 = int(input('Digite o segundo valor: '))
    soma = n1 + n2
    print('A soma é igual a ', soma)
elif opcao == 2:
    print('Opção 2 selecionada')
    valor = int(input('Digite o número: '))
    raiz = valor ** (1 / 2)
    print('A raiz quadrada é: ', raiz)