safes = 0
def direction(number):
    if number < 0:
        return -1
    return 1



with open("input.txt", "r") as f:
    file = f.readlines()
 
    for line in file:
        level = line.split(" ")
        for i in range(len(level)):
            level[i] = int(level[i])
        
        number = level[0] - level[1]
        sentido = direction(number)

        
