# 3. Cadastro de filme
# Crie um dicionário contendo: título, diretor e ano.
# Exiba todas as informações formatadas.

filme = {
    'titulo': 'A Estrada Escura',
    'diretor': 'Cleiton Camargo',
    'ano': 1984,
}

titulo_filme = filme.get('titulo', 'Filme não encontrado')
diretor_filme = filme.get('diretor', 'Diretor não encontrado')
ano_filme = filme.get('ano', 'Ano não encotrado')
print(f'O nome do filme é: {titulo_filme}')
print(f'O diretor do filme é: {diretor_filme}')
print(f'O ano do filme é: {ano_filme}')

# OU POR ITERAÇÃO NO DICIONÁRIO:

for chave, valor in filme.items():
    print(f'{chave}: {valor}')