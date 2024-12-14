import re
import numpy as np
f = open("data.txt", "r")
data = f.read().split("\n")

def findNumberOfToken(buttonA,buttonB,prize):
    A = np.array([[buttonA[0],buttonB[0]],[buttonA[1],buttonB[1]]])
    B =  np.array([prize[0],prize[1]])
    X = np.linalg.solve(A , B)
    a,b = round(X[0]), round(X[1])

    # remove comment for 1
    # if a > 100 or b > 100:
    #     return 0

    if  a * buttonA[0] + b * buttonB[0] == prize[0] and a * buttonA[1] + b * buttonB[1] == prize[1]:
        return a*3 +b

    else:
        return 0

pattern = r"(\d+)"
sum = 0
for i in range(len(data)):
    if data[i]:
        result = list(map(int,re.findall(pattern,data[i])))

        #4 cause skipping ''
        if i % 4 == 0:
            buttonA = result

        elif i % 4 == 1:
            buttonB = result

        elif i % 4 == 2:
            prize = result
            #put comment for 1
            prize[0] = 10000000000000+result[0]
            prize[1] = 10000000000000+result[1]
            sum += findNumberOfToken(buttonA,buttonB,prize)

print(sum)
