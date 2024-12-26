safes = 0
def direction(number):
    if number < 0:
        return -1
    return 1


def checa (level, pos):
    lista = level.copy()

    lista.pop(pos)
    for i in range(len(lista)-1):
        change = (lista[i]-lista[i+1])
        if (change*sentido < 0) or (abs(change) > 3) or (abs(change) < 1):
            return False
    
    return True
    


with open("input.txt", "r") as f:
    file = f.readlines()
 
    for line in file:
        level = line.split(" ")
        for i in range(len(level)):
            level[i] = int(level[i])
        
        number = level[0] - level[1]
        sentido = direction(number)

        safes += 1

        for i in range(len(level)-1):
            change = (level[i]-level[i+1])
            if (change*sentido < 0) or (abs(change) > 3) or (abs(change) < 1):
                if checa(level, i) or checa(level, i+1):
                    break
                else:
                    safes -= 1



print(safes)
