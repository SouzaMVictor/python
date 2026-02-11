def mover_discos(num_discos, origem, destino, auxiliar):
    if num_discos == 1:
        print(f'mover disco 1 da {origem} para {destino}')
    else:
        mover_discos(num_discos - 1, origem, auxiliar, destino)
        print(f'mover disco {num_discos} da {origem} para {destino}')
        mover_discos(num_discos - 1, auxiliar, destino, origem )
mover_discos(2, "torre 1", "torre 3", "torre 2" )