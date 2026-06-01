# 2. Cores favoritas
# Crie um conjunto com 5 cores.
# Peça ao usuário uma cor e informe se ela já está cadastrada ou não.

cores = { 
    "Azul",
    "Vermelho",
    "Amarelo",
    "Cinza",
    "Preto",
}

cor = input('Digite o nome de uma cor: ').capitalize()

if cor in cores:
    print('A cor está cadastrada.')
else:
    print('A cor NÃO está cadastrada.')