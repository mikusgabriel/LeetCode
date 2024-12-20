import random
from copy import deepcopy
from itertools import permutations

f = open("data.txt", "r")
input = f.read().strip().split("\n")

towel_list = [x.strip() for x in input[0].split(",")]
towel_list.sort(key=len, reverse=True)
test_list = input[2:]
test_list_test2 = deepcopy(test_list)

def test1():
    summ = 0

    for i in range(len(test_list)):
        t = 0
        random_towel_list = deepcopy(towel_list)
        word = deepcopy(test_list[i])

        while t < 1000:
            test_list[i] = word
            for towel in random_towel_list:
                if towel in test_list[i]:
                    test_list[i] = test_list[i].replace(towel, "0")

            if test_list[i].replace("0", "") == "":
                summ += 1
                break

            random.shuffle(random_towel_list)
            t += 1


    return summ

def test2():
  


   pass



print(test1())
