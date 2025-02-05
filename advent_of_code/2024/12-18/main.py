from collections import deque
from copy import deepcopy
f = open("data.txt", "r")


data = f.read().strip().split("\n")

set_pos = set()
next_inline = []
for p in range(len(data)):
    if p >= 1024:
        next_inline.append(tuple(int(element) for element in data[p].split(",")))
    else:
        set_pos.add(tuple(int(element) for element in data[p].split(",")))



height = 71
width = 71

# Create a matrix of zeros
matrix = [[0 for _ in range(width)] for _ in range(height)]

# Set the positions in the matrix to 1
for col,row  in set_pos:
    if 0 <= row < height and 0 <= col < width:  # Ensure positions are within bounds
        matrix[row][col] = 1

# Print the matrix (optional, for visualization)
for row in matrix:
    print(row)



def inBounds(i, j):
    if i < 0 or j < 0:
        return False
    elif i >= height or j >= width:
        return False
    return True


def pathFind(i,j,step):
    visited = set([(0,0)])
    

    queue = deque([(0,0,0)])

    while queue:

        (i,j,step) = queue.popleft()

        if (i,j) == (height-1,width-1):
            return step
        
        combination = [[-1,0],[1,0],[0,1],[0,-1]]
        
        for comb in combination:

            new_i = i + comb[0]
            new_j = j + comb[1]

            if (new_j,new_i) not in set_pos and (new_j,new_i) not in visited:

                if inBounds(new_i,new_j):
                    visited.add((new_j,new_i))
                    queue.extend([(new_i,new_j,step+1)])




initial_bytes = 12
cmp = 0
while True:
    print(cmp)
    set_pos.add(next_inline[cmp])

    if not pathFind(0,0,0):
        print(f"{next_inline[cmp][0]},{next_inline[cmp][1]}")
        break

    cmp+=1


                   

                
