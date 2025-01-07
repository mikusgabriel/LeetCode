def isValid(line):
    numbers = [int(x) for x in line.split()]
    if len(line) == 0:
        return False
    
    descending = False
    difference = 0
    for i in range(len(numbers)-1):
        difference += numbers[i] - numbers[i+1]

    if difference > 0:
        descending = True

    for i in range (len(numbers)-1):
        if descending is True:
            if numbers[i] - numbers[i+1] > 0 and  numbers[i] - numbers[i+1] < 4:
                pass                    

            else:
                return False
        elif descending is False:
            if numbers[i] - numbers[i+1] < 0 and numbers[i] - numbers[i+1] > -4:
                pass
            else:
                return False
            
    return True


        

def partTwo(line):
    new_array = []
    for i in range(len(line)):
        new_array = line[:i] + line[i+2:]
        if isValid(new_array):
            return True

    return False  








    




f = open("data.txt", "r")
arr = f.read().split("\n")

summ = 0
for line in arr:
    if isValid(line):
        summ+=1
    elif partTwo(line):
        summ+=1
print(summ)
