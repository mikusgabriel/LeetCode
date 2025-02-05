f = open("data.txt", "r")
antenna_matrix = f.read().split("\n")

lenght = len(antenna_matrix) -1
width = len(antenna_matrix[0])
antinode_matrix = ["."] * lenght
for i in range(len(antinode_matrix)):
    antinode_matrix[i] = ["."] * width


#a verifier si ca marche
def placeAntiNodes(i1,j1,i2,j2):
    placed = 0
    
    difference_i = i2 - i1
    difference_j = j2 - j1
        
    antinode_1 = [i1 - difference_i, j1 - difference_j]
    antinode_2 = [i2 + difference_i, j2 + difference_j]

    while True:

        if check_bounds(antinode_1):
            if antinode_matrix[antinode_1[0]][antinode_1[1]] == ".":
                antinode_matrix[antinode_1[0]][antinode_1[1]] = "X"
                placed += 1
        else:
            break

        antinode_1 = [antinode_1[0] - difference_i, antinode_1[1] - difference_j]
       

    while True:
       
        if check_bounds(antinode_2):
            if antinode_matrix[antinode_2[0]][antinode_2[1]] == ".":
                antinode_matrix[antinode_2[0]][antinode_2[1]] = "X"
                placed += 1
        else:
            break  

        antinode_2 = [antinode_2[0] + difference_i, antinode_2[1] + difference_j]

    
    if antinode_matrix[i1][j1] == ".":
        antinode_matrix[i1][j1] = "X"
        placed += 1

    if antinode_matrix[i2][j2] == ".":
        antinode_matrix[i2][j2] = "X"
        placed += 1

# 762

    return placed

def check_bounds(emplacement):
    if emplacement[0] < 0 or emplacement[0] >= lenght:
        return False
    elif emplacement[1] < 0 or emplacement[1] >= width:
        return False
    return True

    
antennas = {}
summ = 0
for i in range(lenght):
    for j in range(width):
        emplacement = antenna_matrix[i][j]
        if emplacement != ".":

            if emplacement in antennas:
                
                for antenna in antennas[emplacement]:
                    placed = placeAntiNodes(i,j,antenna[0],antenna[1])
                    summ += placed

                antennas[emplacement].append([i,j])
            else:
                antennas[emplacement] = [[i,j]]

print("test1:", 228)
print("test2:", summ)

