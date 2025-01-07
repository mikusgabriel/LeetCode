import re
f = open("data.txt", "r")


data = f.read().strip().split("\n")

pattern = r"-?\d+"

    
robot_pos = []
robot_vel = []

lenght = 103
width = 101


for line in data:
    line_info = re.findall(pattern,line)

    robot_pos.append([int(line_info[0]),int(line_info[1])])
    robot_vel.append([int(line_info[2]),int(line_info[3])])



def inBounds(i, j):
    if i < 0 or j < 0:
        return False
    elif i >= lenght or j >= width:
        return False
    return True


def simulate100s():



   
    #put for _ in 100 for the first test
    k = 1
    while True:
        print(k-1)

        set_of_tuples = set(tuple(sublist) for sublist in robot_pos)

        if len(robot_pos) == len(set_of_tuples):
                   # Create a matrix of zeros
            matrix = [[0 for _ in range(width)] for _ in range(lenght)]

            # Set the positions in the matrix to 1
            for col, row  in robot_pos:
                if 0 <= row < lenght and 0 <= col < width:  # Ensure positions are within bounds
                    matrix[row][col] = 1

            # Print the matrix (optional, for visualization)
            for row in matrix:
                print(row)

            break
            

     


        for i in range(len(robot_pos)):

            robot_pos[i][0] += robot_vel[i][0]
            robot_pos[i][1] += robot_vel[i][1]

            #maybe wrong
            if not inBounds(robot_pos[i][1],robot_pos[i][0]):
                tuple_new_pos = teleport(robot_pos[i][1], robot_pos[i][0])

                robot_pos[i][0] = tuple_new_pos[1]
                robot_pos[i][1] = tuple_new_pos[0]

        k+=1
     



cases = [(lenght,width),(0,width),(lenght,0),(0,-width),(-lenght,0),(-lenght,-width),(-lenght,width),(lenght,-width)]



def teleport(i,j):

    for case in cases:

        new_i = i + case[0]
        new_j = j + case[1]

        if inBounds(new_i,new_j):
            return (new_i,new_j)
        


simulate100s()

middle_hori = lenght//2
middle_verti = width//2

quadrants = [[],[],[],[]]

for robot in robot_pos:

    if robot[0] < middle_verti and robot[1] < middle_hori:
        quadrants[0].append(robot)

    elif robot[0] < middle_verti and robot[1] > middle_hori:
        quadrants[2].append(robot)

    elif robot[0] > middle_verti and robot[1] < middle_hori:
        quadrants[1].append(robot)

    elif robot[0] > middle_verti and robot[1] > middle_hori:
        quadrants[3].append(robot)

summ = 1
for list in quadrants:
    summ *= len(list)

print(summ)
