# Dada a lista valores = [25, 14, 89, 7, 42, 95, 63, 95, 22], escreva um programa que encontre o segundo maior valor presente na lista.
# Restrição: Você não pode usar funções de ordenação sort() ou sorted() para resolver este problema. A lógica deve ser implementada usando um laço de repetição.
# Dica: Você precisará de duas variáveis para guardar o maior e o segundo maior valor enquanto percorre a lista.


valores = [25, 14, 89, 7, 42, 95, 63, 95, 22]
maior = float('-inf') #-inf = menos infinito
segundoMaior = float('-inf')

for valor in valores:
    if valor > maior:
        segundoMaior = maior
        maior = valor
    elif valor > segundoMaior and valor != maior:
        segundoMaior = valor
print(segundoMaior)
