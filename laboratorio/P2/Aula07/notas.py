arq = open('turma.txt', 'r')
dados = arq.readlines()
arq.close()
saida = open('medias.txt', 'w')
saida.write('Nome, Média')
for i in range(1, len(dados)):
    aluno = dados[i].split(',')
    nome = aluno[0]
    soma = 0
    for j in range(1, len(dados)):
        soma += float(aluno[j])
    media = soma / (len(aluno)-1)
    linha = nome + "," + str(media) + "\n"
    saida.write(linha)
saida.close()

    

# OU 

arquivo = open('turma.txt', 'r')

for linha in range(1, len(arquivo)):
    linha = arquivo.readline()
    aluno = linha..strip().split(',')
    # nome, n1, n2, n3 = linha.split(',')
    nome = aluno[0]
    notaP1 = float(aluno[1])
    notaP2 = float(aluno[2])
    notaP3 = float(aluno[3])
    
    mediaAluno = (notaP1 + notaP2 + notaP3) / 3
    print(aluno, mediaAluno)

arquivo.close()
    
