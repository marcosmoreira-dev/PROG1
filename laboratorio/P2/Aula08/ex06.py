arquivo = open('estoque.txt', 'r')
dados = arquivo.readlines()
arquivo.close()

saida = open('estoque_atualizado.txt', 'w')

for i in range(len(dados)):
    dados_split = dados[i].strip().split(',')
    produto = dados_split[0]
    codigo = dados_split[1]
    vendas = int(dados_split[2])
    quantidade = int(dados_split[3])
    preco = float(dados_split[4])
    
    if (vendas / quantidade) <= 0.2:
        preco -= preco * 0.1

    linha = produto + ',' + codigo + ',' + str(vendas) + ',' + str(quantidade) + ',' + str(preco)
    saida.write(linha + '\n')

saida.close()
