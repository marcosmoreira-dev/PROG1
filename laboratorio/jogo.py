forca = int(input('Digite a força do herói: '))
dano = int(input('Digite o dano da arma: '))
energia = float(input('Digite a energia atual: '))

ataque = forca + dano

if energia > 50:
    ataqueFinal = ataque * 1.2
elif energia <= 50 and forca > 80:
    ataqueFinal = ataque
elif energia <= 50 and forca <= 80:
    ataqueFinal = ataque - (ataque * 0.3)
print(f'O valor do ataque final é igual a {ataqueFinal:.1f}')

