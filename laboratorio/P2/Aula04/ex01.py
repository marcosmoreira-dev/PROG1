# Crie uma lista que armazene 3 tuplas, onde cada tupla representa uma coordenada (lat, long). Peça ao usuário para digitar uma nova coordenada, verifique se ela já existe na lista e exiba uma mensagem de "Local já registrado" ou "Novo local adicionado".

coord = [(1,3),(4.5,8),(7.2,1.1)]
lat = float(input("Informe latitude"))
lon = float(input("Informe longitude"))
nova_coord = (lat,lon)

if nova_coord in coord:
    print("Local registrado")

else:
    coord.append(nova_coord)
    print("Novo local adicionado")