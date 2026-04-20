# Não corrigido

salario = float(input('Digite o salário: '))

if salario <= 300:
    aumento = 0.5
elif salario > 300 and salario <= 500:
    aumento = 0.4
elif salario > 500 and salario <= 700:
    aumento = 0.3
elif salario > 700 and salario <= 800:
    aumento = 0.2
elif salario > 800 and salario <= 1000:
    aumento = 0.1
elif salario > 1000:
    aumento = 0.05

novoSalario = salario * aumento

print(f'O novo salário é igual a: {novoSalario}')