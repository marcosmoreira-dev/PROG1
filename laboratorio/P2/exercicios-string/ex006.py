# Peça ao usuário para inserir uma frase. O programa deve analisar a frase e exibir as seguintes informações:
# O número total de caracteres (incluindo espaços)
# O número de vogais
# O números de consoantes
vogais = 'AEIOU'
consoantes = 'BCDFGHJKLMNPQRSTVWXYZ'

frase = input('Digite uma frase: ')
frase1 = frase.upper()
tam = len(frase)
contVogais = 0
contCons = 0

for letra in frase1:
    if letra in vogais:
        contVogais += 1
    elif letra in consoantes:
        contCons += 1

print(f'O tamanho da frase é {tam}')
print(f'A quantidade de vogais é igual a: {contVogais}')
print(f'A quantidade de consoantes é igual a: {contCons}')

# OU
# contv = 0
# contc = 0
# vogais = 'AEIOU'
# consoantes = 'BCDFGHJKLMNPQRSTVWXYZ'
# texto = input('Digite o texto')
# tam = len(texto)
#
# for i in range(tam):
#   if texto[i] in vogais:
#       contv += 1
#   elif texto[i] in cons:
#       contc += 1
#
# print(tam)
# print(conv)
# print(conc)