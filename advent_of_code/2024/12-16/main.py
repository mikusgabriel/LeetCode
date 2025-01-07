import re
from collections import deque
from copy import deepcopy

f = open("data.txt", "r")
matrix = f.read().strip().split()


patternStart = r"S"
patternEnd = r"E"

start_pos = (0, 0)
end_pos = (0, 0)

for i in range(len(matrix)):
    start_pos_re = re.search(patternStart, matrix[i])
    if start_pos_re:
        start_pos = (i, start_pos_re.span()[0])

    end_pos_re = re.search(patternEnd, matrix[i])
    if end_pos_re:
        end_pos = (i, end_pos_re.span()[0])

print(start_pos)
print(end_pos)


# def bfs():
#     points = []

#     # print(simulated_matrix)

#     visited = set([(start_pos[0],start_pos[1])])

#     queue = deque([(start_pos[0],start_pos[1],0,0)])

#     while queue:
#         # print(queue)

#         (i,j,steps,turns) = queue.popleft()


#         if (i,j) == end_pos:
#             points.append(steps+turns)
#             continue

#         print(queue)

#         cases = [[0,1],[0,-1],[1,0],[-1,0]]

#         for case in cases:

#             new_i = i + case[0]
#             new_j = j + case[1]

#             if (new_i,new_j) not in visited and matrix[new_i][new_j] != "#":

#                 visited.add((new_i,new_j))
#                 queue.extend([(new_i,new_j,steps+1,turns)])

#     return points
points = []


# changer position de depart
visited = set([(start_pos[0], start_pos[1], 0, ("^"))])


def dfs(i, j, steps, turns):
    if (i, j) == end_pos:
        points.append(steps + (len(turns) * 1000))
        return True

    cases = {">": (0, 1), "<": (0, -1), "^": (1, 0), "_": (-1, 0)}

    for case, (di, dj) in cases.items():
        new_i, new_j = i + di, j + dj

        turns = list(turns)
        turns.append(case)
        turns = tuple(turns)

        new_turns = tuple(turns + (case,))

        if (new_i, new_j, steps + 1, len(new_turns)) not in visited and matrix[new_i][
            new_j
        ] != "#":
            # Mark the position as visited
            visited.add((new_i, new_j, steps + 1, len(new_turns)))

            # Recursively call dfs for the next step
            dfs(new_i, new_j, steps + 1, new_turns)

    return points


print(dfs(start_pos[0], start_pos[1], 0, ("^")))
print(points)
