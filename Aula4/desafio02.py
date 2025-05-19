elementos = [5,2,5,8,1,8,3]

sem_repetidos = []
for item in elementos:
    if item not in sem_repetidos:
        sem_repetidos.append(item)

print(sem_repetidos)