import re
from collections import deque
from copy import deepcopy

f = open("data.txt", "r")
matrix = f.read().strip().split()


patternStart = r"S"
patternEnd = r"E"

start_pos = (0,0)
end_pos = (0,0)

for i in range(len(matrix)):
    
  
    start_pos_re = re.search(patternStart,matrix[i])
    if start_pos_re:
        start_pos = (i,start_pos_re.span()[0])

    end_pos_re = re.search(patternEnd,matrix[i])
    if end_pos_re:
        end_pos = (i,end_pos_re.span()[0])

print(start_pos)
print(end_pos)

kart_pos = start_pos

def inBounds(i, j):
    if i < 0 or j < 0:
        return False
    elif i >= len(matrix) or j >= len(matrix[0]):
        return False
    return True



def bfs(moment,direction):


    simulated_matrix = [list(row) for row in deepcopy(matrix)]

    # print(simulated_matrix)

    visited = set([(kart_pos[0],kart_pos[1])])
    
    queue = deque([(kart_pos[0],kart_pos[1],0)])

    while queue:
        # print(queue)

        (i,j,picos) = queue.popleft()

        if moment == picos:
            for _ in range(2):
                if (i+direction[0],j+direction[1]) != end_pos:
                    simulated_matrix[i+direction[0]][j+direction[1]] = "."
                else:
                    break


        if (i,j) == end_pos:
            return (9308-picos)
    


        cases = [[0,1],[0,-1],[1,0],[-1,0]]

        for case in cases:

            new_i = i + case[0]
            new_j = j + case[1]

            if inBounds(new_i,new_j) and (new_i,new_j) not in visited and simulated_matrix[new_i][new_j] != "#":

                visited.add((new_i,new_j))
                queue.extend([(new_i,new_j,picos+1)])


summ = 0
#9308
#84

for pico in range(9308):

    print(pico)

    cases = [[0,1],[0,-1],[1,0],[-1,0]]

    for case in cases:
        
        result = bfs(pico,case)

        if result >= 100:
            summ +=1




print(summ)


#test 2 is 20 more cheats
