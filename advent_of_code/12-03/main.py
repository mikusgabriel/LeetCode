import re


f = open("data.txt", "r")
arr = f.read()


def premier_test(string):
    summ = 0
    matches = re.findall(r"mul\((\d+),(\d+)\)", arr)

    for i in range(len(matches)):
        summ += int(matches[i][0]) * int(matches[i][1])

    print("test1 result:",summ)

premier_test(arr)


def deuxieme_test(string):
    dont = False
    summ = 0
    matches = re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don\'t\(\))", string)
    
    for i in range(len(matches)):
        if matches[i][0] and matches[i][1]:
            if dont is False:
                summ+= int(matches[i][0])*int(matches[i][1])
        elif matches[i][2]:
            dont = False
        elif matches[i][3]:
            dont = True
    print("test2 result:",summ)

deuxieme_test(arr)
