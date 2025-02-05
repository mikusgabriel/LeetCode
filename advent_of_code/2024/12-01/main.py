


f = open("data.txt", "r")
arr = f.read().split()

left_list = []
right_list = []

for i in range(len(arr)):
    if i % 2 == 0:
        right_list.append(int(arr[i]))
    else:
        left_list.append(int(arr[i]))

left_list.sort()
right_list.sort()

distance = 0

for i in range(len(left_list)):
    temp_distance = left_list[i] - right_list[i]

    if temp_distance < 0:
        distance += (-1 * temp_distance)
    
    else:
        distance += temp_distance

print(distance)

hashmap_right = {}
for i in range(len(right_list)):
    if right_list[i] in hashmap_right:
        hashmap_right[i] += 1
    else:
        hashmap_right[right_list[i]] = 1

similarity_score = 0
for i in range(len(left_list)):
    if left_list[i] in hashmap_right:
        similarity_score += left_list[i] * hashmap_right[left_list[i]]
        
print(similarity_score)
