from copy import deepcopy


f = open("data.txt", "r")
line_input = f.read().strip()


def generateFileSystem_checksum(line_input):

    filesystem_checksum = []
    id_number = 0
    for i in range(len(line_input)):
        if i % 2 == 0:
            for j in range(int(line_input[i])):
                filesystem_checksum.append(id_number)

            id_number+=1

        else:
            for j in range(int(line_input[i])):
                filesystem_checksum.append(".")
                
    return filesystem_checksum

filesystem_checksum = generateFileSystem_checksum(line_input)



def compactingListTest1(filesystem_checksum):

    filesystem_array = filesystem_checksum
    result = []
    i = 0
    while True:

        if filesystem_array[i] == ".":
            for j in range(len(filesystem_array),0,-1):
                moved_file = filesystem_array.pop()
                if moved_file != ".":
                    result.append(moved_file)
                    break

        else:
            result.append(filesystem_array[i])

        i+=1

        if i>= len(filesystem_array):
            return result


def checkSummOfFile(result):
    summ = 0
    for i in range(len(result)):
        summ += i * int(result[i])
    return summ





result = compactingListTest1(filesystem_checksum)
summ = checkSummOfFile(result)




def generateFileSystem_checksumTest2(line_input):
    
    filesystem_checksum = []
    id_number = 0
    for i in range(len(line_input)):
        if i % 2 == 0:
            temp = []
            for j in range(int(line_input[i])):
                temp.append(id_number)
            filesystem_checksum.append(temp)
            id_number+=1

        else:
            temp = []
            for j in range(int(line_input[i])):
                temp.append(".")
            filesystem_checksum.append(temp)
                
    return filesystem_checksum

def compactingListTest2(file_system_list):

    filesystem_array = file_system_list
    i = len(filesystem_array)-1
    while True:

        if filesystem_array[i]:
            if filesystem_array[i][0] != ".":
                for j in range(0,i):
                    
                    if filesystem_array[j]:
                        if filesystem_array[j][0] == ".":
                            lenghtContainerSpace = len(filesystem_array[j])

                            if len(filesystem_array[i]) == lenghtContainerSpace:
                                filesystem_array[j] = filesystem_array[i]
                                filesystem_array[i] = ['.'] * len(filesystem_array[i])
                                break
                            elif len(filesystem_array[i]) < lenghtContainerSpace:
                                difference  = lenghtContainerSpace -  len(filesystem_array[i]) 
                                filesystem_array[j] = filesystem_array[i]
                                filesystem_array[i] = ['.'] * len(filesystem_array[i])
                                array = ['.'] * difference
                                filesystem_array.insert(j+1,array)
                                break
                            

        i-=1

        if i<=1 :
            return filesystem_array

def checkSummOfFile2(result):
    summ = 0
    counter = 0
    for i in range(len(result)):
        if isinstance(result[i],list):
            for j in range(len(result[i])):
                if result[i][j] != ".":
                    summ += counter * int(result[i][j])
                counter +=1
        else:
            if result[i] != ".":
                summ += counter * result[i]
            counter +=1    
    return summ


filesystem_checksum2 = generateFileSystem_checksumTest2(line_input)
result2 = compactingListTest2(filesystem_checksum2)
summ2 = checkSummOfFile2(result2)







print("test1",summ)
print("test2",summ2)
