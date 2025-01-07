import re
import copy 
import math
f = open("data.txt", "r")

tab = f.read().split("\n")
tab = tab[:-1]

position_guard = [0, 0]
guard_sign = "^"
positions_visited = {}
for y in range(len(tab)):
    for x in range(len(tab[y])):
        if tab[y][x] == guard_sign:
            position_guard = [x, y]
            positions_visited[(position_guard[0], position_guard[1])] = 0
            break

bounds_vertical = len(tab)
bounds_horizontal = len(tab[0])


def getLine(pos, direction):
    line = ""

    if direction == 0:
        # up
        for i in range(pos[1], -1, -1):
            line += tab[i][pos[0]]

    elif direction == 1:
        # right
        for i in range(pos[0], bounds_horizontal):
            line += tab[pos[1]][i]

    elif direction == 2:
        # down
        for i in range(pos[1], bounds_vertical):
            line += tab[i][pos[0]]

    elif direction == 3:
        # left
        for i in range(pos[0], -1, -1):
            line += tab[pos[1]][i]

    return line


def changeGuardPos(direction, guard,in_simulation):
    if direction == 0:
        # up
        if in_simulation is False:
            if (guard[0], guard[1] - 1) not in positions_visited:
                positions_visited[(guard[0], guard[1] - 1)] = direction
        guard[1] -= 1

    elif direction == 1:
        # right
        if in_simulation is False:
            if (guard[0] + 1, guard[1]) not in positions_visited:
                positions_visited[ (guard[0] + 1, guard[1])] = direction


        guard[0] += 1

    elif direction == 2:
        # down
        if in_simulation is False:
            if (guard[0], guard[1] + 1) not in positions_visited:
                positions_visited[(guard[0], guard[1] + 1)] = direction

      

        guard[1] += 1

    elif direction == 3:
        # left
        if in_simulation is False:
            if (guard[0] - 1, guard[1]) not in positions_visited:
                positions_visited[(guard[0] - 1, guard[1])] = direction

      
        guard[0] -= 1



def test1():
    pattern = r"#"
    cmp = 0
    summ_of_obstacle = 0
    test_counter = 0
    while True:
        direction = cmp % 4
        line = getLine(position_guard, direction)

        regex_match = re.search(pattern, line)

        if regex_match is None:
            for z in range(len(line)-1):

               
                changeGuardPos(direction, position_guard,False)

            break 

        index_movement = regex_match.span()[0] - 1
        for i in range(index_movement):
            
            changeGuardPos(direction,position_guard,False)

        
        cmp += 1

    return (len(positions_visited),summ_of_obstacle)

# def test2(guard_position,direction,simulated_hash_pos,line,index):
#     pattern = r"#"
#     cmp = 0
    
#     regex_match = re.search(pattern, line)
#     if regex_match is None:
#             return False
        

#     if  abs(regex_match.span()[0] - guard_position[0]) >= 1 and abs(regex_match.span()[0] - guard_position[1]) >= 1 and abs(regex_match.span()[1] - guard_position[0]) >= 1 and abs(regex_match.span()[1] - guard_position[0]) >= 1:


#         direction = direction+1 % 4

#         while True:
#             direction = direction % 4
#             line = getLine(guard_position, direction)
#             regex_match = re.search(pattern, line)
            

#             if regex_match is None:
#                 return False
           
#             if cmp>=10000:
#                 return True
                
            
#             index_movement = regex_match.span()[0] - 1

#             for i in range(index_movement):
               
#                 changeGuardPos(direction,guard_position,True)
#                 guard_tuple = (guard_position[0],guard_position[1])
#                 if guard_tuple in simulated_hash_pos and simulated_hash_pos[guard_tuple] == direction:
#                     return True
               
#             direction +=1
#             cmp +=1
                
#     else:
#         print("sds")
#         return False

#CHATGPT I COULDNT FINISH WITH MINE
def turn_right(d):
    return {'^': '>', '>': 'v', 'v': '<', '<': '^'}[d]

def forward(r, c, d):
    if d == '^': return r-1, c
    if d == 'v': return r+1, c
    if d == '<': return r, c-1
    if d == '>': return r, c+1

def in_bounds(r, c, R, C):
    return 0 <= r < R and 0 <= c < C

def neighbors(r, c):
    return [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]

def solve_part2(grid):
    R, C = len(grid), len(grid[0])
    sr = sc = sd = None
    for i in range(R):
        for j in range(C):
            if grid[i][j] in '^v<>':
                sr, sc, sd = i, j, grid[i][j]
                break
        if sr is not None:
            break
    def simulate(obs):
        r, c, d = sr, sc, sd
        s = set()
        steps = 0
        while 0 <= r < R and 0 <= c < C:
            nr, nc = forward(r, c, d)
            if not in_bounds(nr, nc, R, C): return False, None
            if (nr,nc) == obs:
                d = turn_right(d)
            elif grid[nr][nc] == '#':
                d = turn_right(d)
            else:
                r, c = nr, nc
                if (r,c,d) in s: return True, s
                s.add((r,c,d))
            steps += 1
            if steps > R*C*10: 
                return False, None
        return False, None
    candidates = 0
    for i in range(R):
        for j in range(C):
            if (i,j) == (sr,sc): 
                continue
            if grid[i][j] == '#': 
                continue
            loop, _ = simulate((i,j))
            if loop:
                candidates += 1
    return candidates

with open("data.txt") as f:
    grid = [list(line.rstrip('\n')) for line in f if line.strip()]

print(test1())
print(solve_part2(grid))

    
