# Escreva uma função chamada filtrar_por_genero que receba uma lista de dicionários (onde cada dicionário representa um livro com titulo e genero) e uma string com o genero_alvo.
# ● Saída: A função deve retornar uma nova lista contendo apenas os títulos dos livros que pertencem ao gênero solicitado.
# ● Exemplo de Entrada: livros = [{"titulo": "O Hobbit", "genero": "Fantasia"}, {"titulo":"Duna", "genero": "Sci-Fi"}]

livros = [
    {"titulo": "O Hobbit",
     "genero": "Fantasia"
     },
    {"titulo": "Duna",
      "genero": "Sci-Fi",
    },
    ]

def filtraPorGenero(lista, genero_alvo):
    livros = []
    for i in range(len(lista)):
        livro = lista[i]
        if livro["genero"] == genero_alvo:
            livros.append(livro['titulo'])
    return livros

# OU 

def filtraPorGenero2(lista, genero_alvo):
    livros = []
    for livro in lista:
        if livro["genero"] == genero_alvo:
            livros.append(livro['titulo'])
    return livros




