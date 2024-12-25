def distance(value1, value2):
    return abs(value1 - value2)

left_values = []
right_values = []

def count_examples(value):
    position = 0
    counts = 0
    while position < len(right_values):
        if value == right_values[position]:
            counts += 1
            #right_values.pop(position)
        position +=1
    return counts



with open("input.txt", "r") as f:
    file = f.readlines()
    
    for line in file:
        split = line.split("   ")
        left_values.append(int(split[0]))
        right_values.append(int(split[1]))
        #print(line)

# Solves part 1

left_values.sort()
right_values.sort()
#print(left_values)

# dists = []

# for i in range(len(left_values)):
#     dists.append(distance(left_values[i], right_values[i]))

# print(sum(dists))

# Solves part 2

count_values = 1
values_counts = []
left_length = len(left_values)
position = 0

while position < left_length - 1:
    if left_values[position] == left_values[position+1]:
        count_values += 1
    else:
        count = count_examples(left_values[position])
        result = count * count_values * left_values[position]
        values_counts.append(result)
        count_values = 1
    
    position += 1


values_counts.append(count_examples(left_values[left_length-1]) * left_values[left_length-1])

print(sum(values_counts))







