# Você recebeu uma lista de string, onde cada string contém o nome de um aluno, seguido por suas notas, separadas por vígurlas. Seu objetivo é processar esses dados para calcular a média de cada aluno e determinar seu status de aprovação. A média para a aprovação é 7.0

dados_alunos = [
    "Ana Silva: 8.5, 9.0, 7.5",
    "Bruno Costa: 6.0, 5.5, 7.0",
    "Carla Dias: 9.5, 10.0, 9.0"
]

for i in range(len(dados_alunos)):
    dados_split = dados_alunos[i].split(': ') # [NOME, NOTAS]
    nome = dados_split[0]
    notas = dados_split[1].split(',') # [NOTA1, NOTA2, NOTA3]
    soma = 0
    for j in range(len(notas)):
        soma = soma + float(notas[j])
    media = soma / (len(notas))
    if media >= 7.0:
        status = "Aprovado"
    else: 
        status = 'Reprovado'
    print(f"{nome} | Média: {media:.1f} | Status: {status}")


    


