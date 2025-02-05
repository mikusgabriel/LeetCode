import math
import time
debut_time = time.time()
# If the stone is engraved with the number 0,
# it is replaced by a stone engraved with the number 1.

# If the stone is engraved with a number that has an even number of digits, it is replaced by two stones.
# The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone.
# (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)

# If none of the other rules apply, the stone is replaced by a new stone;
# the old stone's number multiplied by 2024 is engraved on the new stone.
f = open("data.txt", "r")
rocks_array = list(map(int, f.read().strip().split()))
print(rocks_array)

memoSplit = {}

def getResultCompute(number,f):
    if f >= 75:
        return 1
    if (number,f) in memoSplit:
            return memoSplit[(number,f)]
    if number == 0:
        result = getResultCompute(1,f+1)
        memoSplit[(number,f)] = result
        return result
  

    length_number = math.floor(math.log10(number)) + 1



    if length_number % 2 != 0:
        result = getResultCompute(number*2024,f+1)
        memoSplit[(number,f)] = result
        return result
    
    left_part = number // 10 ** (length_number / 2)
    right_part = number % 10 ** (length_number / 2)
    
    

    result =  getResultCompute(left_part,f+1) + getResultCompute(right_part,f+1)
    memoSplit[(number,f)] = result


    return result

summ = 0

i = 0
# might fail, lets see if len changes during the loop
length = len(rocks_array)
while i < length:
    summ += getResultCompute(rocks_array[i],0)
    
  
    
    i+=1

print(summ)
print(time.time()-debut_time)
