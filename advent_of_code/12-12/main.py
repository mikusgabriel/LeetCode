from itertools import product

f = open("data.txt", "r")
matrix = f.read().strip().split("\n")

print(matrix)

lenght = len(matrix)
width = len(matrix[0])

region_hashmap = {}


def inBounds(i, j):
    if i < 0 or j < 0:
        return False
    elif i >= lenght or j >= width:
        return False
    return True


def findRegion(i, j, index):
    # print(i,j,index)
    initial_letter = matrix[i][j]

    if (initial_letter, index) not in region_hashmap:
        region_hashmap[(initial_letter, index)] = set()

    region_hashmap[(initial_letter, index)].add((i, j))

    valid_combinations = [
        (a, b)
        for a, b in product([0, 1, -1], repeat=2)
        if (a, b) in [(0, 1), (1, 0), (-1, 0), (0, -1)]
    ]

    for combination in valid_combinations:
        new_j = j + combination[0]
        new_i = i + combination[1]

        if (
            inBounds(new_i, new_j)
            and (new_i, new_j) not in region_hashmap[(initial_letter, index)]
        ):
            if matrix[new_i][new_j] == initial_letter:
                findRegion(new_i, new_j, index)


def getRegionIndex(letter, i, j):
    index = 0
    for key in region_hashmap.keys():
        if letter == key[0]:
            index += 1

            if (i, j) in region_hashmap[key]:
                return 0

    findRegion(i, j, index)


def calculatePerimeter(region):
    perimeter = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for i, j in region:
        for di, dj in directions:
            neighbor_i, neighbor_j = i + di, j + dj

            if (
                not inBounds(neighbor_i, neighbor_j)
                or (neighbor_i, neighbor_j) not in region
            ):
                perimeter += 1

    return perimeter


# compter les coters


for i in range(lenght):
    for j in range(width):
        getRegionIndex(matrix[i][j], i, j)


summ = 0
summ2 = 0
for value in region_hashmap.values():
    perimeter = calculatePerimeter(value)
    perimeter *= len(value)
    summ += perimeter


print(region_hashmap)
print(summ, summ2)
