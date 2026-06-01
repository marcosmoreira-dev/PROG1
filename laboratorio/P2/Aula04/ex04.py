# 4) Peça ao usuário para digitar um texto curto. Transforme o texto em uma lista de palavras e use um conjunto para contar quantas palavras únicas ele utilizou.

texto = input("Informe um texto curto: ")
lista = texto.split()
conjunto = set(lista)
print(f"{len(conjunto)}")

# Outro jeito abaixo 

texto = input()
print(len(set(texto.split())))