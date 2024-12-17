import re
from itertools import product


f = open("data.txt", "r")
line_input = f.read().strip().split("\n")

pattern = r"(\d+)"


def test(goal, equation):
    
    for i in product(["*", "+","||"], repeat=len(equation) - 1):
        compare_goal = 0
        j = 0
        equation_sign_cmp = 0
        while j < len(equation):
            
            if j == 0:
                if i[equation_sign_cmp] == "||":
                    compare_goal = int(str(equation[j]) + str(equation[j + 1]))
                elif i[equation_sign_cmp] == "+":
                    compare_goal = equation[j] + equation[j + 1] 
                elif i[equation_sign_cmp] == "*":
                    compare_goal = equation[j] * equation[j + 1]
                j += 1

            else:
                if i[equation_sign_cmp] == "||":
                    compare_goal = int(str(compare_goal) + str(equation[j]))
                elif i[equation_sign_cmp] == "+":
                    compare_goal += equation[j]
                elif i[equation_sign_cmp] == "*":
                    compare_goal *= equation[j]

                  
            j+=1
            equation_sign_cmp+=1
   
        if compare_goal == goal:

            return goal
        
    return 0

summ = 0
for line in line_input:
    result = re.findall(pattern, line)
   

    equation = list(map(int,result[1:]))
    goal = int(result[0])
    summ += test(goal, equation)

print(summ)
