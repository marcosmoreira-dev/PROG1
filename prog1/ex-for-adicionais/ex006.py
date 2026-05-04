for i in range(15):
    prestacao = float(input('Insira o valor da prestação: '))
    taxa = float(input('Insira o valor da taxa: '))
    
    atraso = prestacao + (prestacao * taxa / 100)
    print(f'Atraso = {atraso}')