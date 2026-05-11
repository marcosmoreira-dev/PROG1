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