# def mover_discos(num_discos, origem, destino, auxiliar):
#     if num_discos == 1:
#         print(f'mover disco 1 da {origem} para {destino}')
#     else:
#         mover_discos(num_discos - 1, origem, auxiliar, destino)
#         print(f'mover disco {num_discos} da {origem} para {destino}')
#         mover_discos(num_discos - 1, auxiliar, destino, origem )
# mover_discos(2, "torre 1", "torre 3", "torre 2" )










# fazendo sozinho para praticar

def mover_discos(numero_discos, origem, auxiliar, destino):
    if numero_discos == 1:
        print(f'mover disco {numero_discos} da {origem} para {destino}')
    else:
        mover_discos(numero_discos - 1, origem, destino, auxiliar)
        print(f'mover disco {numero_discos} da {origem} para {destino}')
        mover_discos(numero_discos -1 , auxiliar, origem, destino)


mover_discos(4, 'torre 1 ', 'torre 2 ', 'torre 3 ')