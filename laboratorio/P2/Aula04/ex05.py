# 5) Crie um dicionário que armazene o nome, o preço e a quantidade em estoque de um produto. Peça ao usuário para atualizar o preço e exiba o dicionário atualizado.

produto = {
    "nome": "guib",
    "preço": 50,
    "quantidade": 10
}

novo_preco = int(input("Informe novo preço: "))
produto["preço"] = novo_preco

print(produto)