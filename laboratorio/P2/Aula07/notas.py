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
    
