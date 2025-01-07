import copy

f = open("data.txt", "r")
arr = f.read().split("\n")

arr = arr[:-1]
page_order_arr = []
update_arr = []

in_update_list = False
for i in range(len(arr)):
    if arr[i] == "":
        in_update_list = True

    else:
        if in_update_list is True:
            temp = arr[i].split(",")
            temp = [int(element) for element in temp]
            update_arr.append(temp)

        else:
            temp = arr[i].split("|")
            temp.reverse()
            temp = [int(element) for element in temp]
            page_order_arr.append(temp)


def getActualPageOrder(update_sublist):
    actual_page_orders = []
    copy_page_order_arr = copy.deepcopy(page_order_arr)

    for i in range(len(copy_page_order_arr)):
        counter = 0
        for j in range(len(update_sublist)):
            if copy_page_order_arr[i][0] == update_sublist[j]:
                counter += 1

            elif copy_page_order_arr[i][1] == update_sublist[j]:
                counter += 1

        if counter == 2:
            actual_page_orders.append(copy_page_order_arr[i])
    return actual_page_orders


def isOrderValid(update_sublist):
    actual_page_orders = getActualPageOrder(update_sublist)

    for i in range(len(update_sublist)):
        if isNumberValid(actual_page_orders,update_sublist[i]) is False:
            return update_sublist
            
    return [update_sublist[len(update_sublist) // 2]]


def isNumberValid(actual_page_orders,number):
    counter = 0
    for j in range(len(actual_page_orders)):
        if actual_page_orders[j]:
            if len(actual_page_orders[j]) == 1:
                if actual_page_orders[j][0] == number:
                    counter += 1
                    actual_page_orders[j].pop()

    for k in range(len(actual_page_orders)):
        if actual_page_orders[k]:
            if len(actual_page_orders[k]) == 2:
                if actual_page_orders[k][0] == number:
                    return False
                        

    for k in range(len(actual_page_orders)):
        if actual_page_orders[k]:
            if actual_page_orders[k][-1] == number:
                actual_page_orders[k].pop()
                counter += 1

    if counter == 0:
        return False
    
    return True
    

def test_two(wrong_update):
    actual_page_orders = getActualPageOrder(wrong_update)
    
    for i in range(len(wrong_update)):
        if  isNumberValid(actual_page_orders,wrong_update[i]) is False:
            for j in range(i+1,len(wrong_update)):
                if isNumberValid(actual_page_orders,wrong_update[j]) is True:
                    temp = wrong_update[i]
                    wrong_update[i] = wrong_update[j]
                    wrong_update[j] = temp
                    break
       
    return wrong_update[len(wrong_update) // 2]




summ1 = 0
summ = 0
for i in range(len(update_arr)):
    response = isOrderValid(update_arr[i])
    
    if len(response) == 1:
        summ1+=response[0]
    else:
        response = test_two(response)
        summ+=response

print("test1:",summ1)
print("test2:",summ)


