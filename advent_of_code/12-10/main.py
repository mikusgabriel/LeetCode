from itertools import product
from copy import deepcopy
f = open("data.txt", "r")
matrix = f.read().strip().split("\n")

for line in matrix:
    print(line)


lenght = len(matrix)
width = len(matrix[0])

def inBounds(i,j):
    if i < 0 or j < 0:
        return False
    elif i >= lenght or j >= width:
        return False
    return True

found_paths_pos= []
# found_paths_set = set()
def getPathsFromPos(i,j,current_index,found_paths_set):
    # if current_index == 0:
        # found_paths_set = set()
    if current_index == 9:
        found_paths_pos.append((i,j))
        # found_paths_set.add((i,j))
        return True
    
    for combination in product([0],[1,-1]):
        combination = list(combination)
        reverse_combination = deepcopy(combination)
        reverse_combination.reverse()
        
        new_i = i + combination[0]
        new_j = j + combination[1]

        new_i2 = i + reverse_combination[0]
        new_j2 = j + reverse_combination[1]

        if inBounds(new_i,new_j) is True:
            if int(matrix[new_i][new_j]) == current_index + 1:
                getPathsFromPos(new_i,new_j,current_index+1,found_paths_set)

        if inBounds(new_i2,new_j2) is True:
            if int(matrix[new_i2][new_j2]) == current_index + 1:
                getPathsFromPos(new_i2,new_j2,current_index+1,found_paths_set)
         

    # return found_paths_set


for i in range(lenght):
    for j in range(width):
        if matrix[i][j] == "0":
            getPathsFromPos(i,j,0,())
            # paths = getPathsFromPos(i,j,0,())
            # for path in paths:
            #     found_paths_pos.append(path)


print(found_paths_pos,len(found_paths_pos))

# comments are test 1 code
