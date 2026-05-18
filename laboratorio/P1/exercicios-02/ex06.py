# Dada a lista valores = [25, 14, 89, 7, 42, 95, 63, 95, 22], escreva um programa que encontre o segundo maior valor presente na lista.
# Restrição: Você não pode usar funções de ordenação sort() ou sorted() para resolver este problema. A lógica deve ser implementada usando um laço de repetição.
# Dica: Você precisará de duas variáveis para guardar o maior e o segundo maior valor enquanto percorre a lista.


valores = [25, 14, 89, 7, 42, 95, 63, 95, 22]

maior = float('-inf')         # Guarda o maior valor encontrado
segundoMaior = float('-inf')  # Guarda o segundo maior valor

# Percorre cada valor da lista
for valor in valores:
    # Verifica se o valor atual é maior que o maior já encontrado
    if valor > maior:
        # Antes de atualizar o maior, o antigo maior vira o segundo maior
        segundoMaior = maior
        maior = valor
    
    # Caso não seja o maior, verifica se ele pode ser o segundo maior
    # Condições:
    # 1. Ser maior que o segundoMaior atual
    # 2. Ser diferente do maior (evita repetir o mesmo valor)
    elif valor > segundoMaior and valor != maior:
        segundoMaior = valor

# Exibe o segundo maior valor da lista
print(segundoMaior)
