arquivo = open('poligonos.txt', 'r')
dados = arquivo.readlines()
arquivo.close()

dados_tupla = []
areas = []

for i in range(len(dados)):
    linha = dados[i].strip().split(',')
    tipo = linha[0]
    base = float(linha[1])
    altura = float(linha[2])

    if tipo == 'RET':
        area = base * altura
    elif tipo == 'TRI':
        area = (base * altura) / 2

    tupla = (tipo, base, altura)
    dados_tupla.append(tupla)
    areas.append(area)

soma = 0
total = len(areas)

for valor in areas:
    soma += valor
    

media = soma / total

print(media)

    