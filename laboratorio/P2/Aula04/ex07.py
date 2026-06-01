# 7) Crie um dicionário onde as chaves são nomes de alunos e os valores são listas contendo 3 notas. O programa deve percorrer o dicionário e exibir o nome de cada aluno junto com a sua média aritmética.

dic = {
    "Claudia": [4,10,8],
    "Lucas": [8,7,5],
    "Marcos": [8,7,9]
}


for chave,valor in dic.items():
    soma = 0 
    for i in valor:
        soma += valor
    media = soma/len(valor)