# Cria a matriz que representa o tabuleiro
tabuleiro = [
    ['X', 'O', 'X'],
    ['O', 'X', 'O'],
    ['O', ' ', 'X']
]

print('--- Tabuleiro do Jogo da Velha ---')

# Laço aninhado para percorrer a matriz
# O laço externo pega cada linha
for i in range(len(tabuleiro)):
    # O laço interno pega cada célula da linha atual
    for j in range(len(tabuleiro[i])):
        print(f' {tabuleiro[i][j] }', end=" | ")
    # Pula uma linha para a próxima fileira do tabuleiro
    print('\n---------------')