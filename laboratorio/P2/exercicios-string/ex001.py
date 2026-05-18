# Crie um programa que receba uma string como argumento e retorne o número de vogais (a, e, i, o, u) que ela contém. O programa deve funcionar tanto para maiúsculas quanto para minúsculas.

texto = input('Digite um texto: ')
vogais = 'AEIOU'
cont = 0
for i in range(len(texto)):
    if texto[i].lower() in vogais:
        cont = cont + 1
print(cont)

# OU

for letra in texto:
    if letra.lower() in vogais:
        cont = cont + 1