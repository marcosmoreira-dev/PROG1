A = int(input('Digite o valor de A: '))
B = int(input('Digite o valor de B: '))

if A <= 0 or B <= 0:
    print('Digite apenas valores inteiros maiores que zero.')
else:
    resultado = 1 # Começamos com 1 (elemento neutro da multiplicação)

# Multiplica A por ele mesmo B vezes
for i in range(B):
    resultado = resultado * A

# Exibe o resultado final
    print(f'{A} elevado a {B} é igual a: {resultado}')

##

# Entrada de dados
a = int(input("Digite a base (A): "))
b = int(input("Digite o expoente (B): "))

resultado = 1

# Multiplicações sucessivas
for i in range(b):
    resultado = resultado * a

print(f"O resultado de {a} elevado a {b} é: {resultado}")