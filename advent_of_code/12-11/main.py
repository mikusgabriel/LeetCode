import math
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
memoMult = {}
for f in range(40):
    i = 0
    # might fail, lets see if len changes during the loop
    length = len(rocks_array)
    while i < length:
        if rocks_array[i] == 0:
            rocks_array[i] = 1
            i += 1
            continue

        length_number = math.floor(math.log10(rocks_array[i])) + 1

        if length_number % 2 == 0:
            if rocks_array[i] in memoSplit:
                left_part = memoSplit[rocks_array[i]][0]
                right_part = memoSplit[rocks_array[i]][1]

            else:
                left_part = rocks_array[i] // 10 ** (length_number / 2)
                right_part = rocks_array[i] % 10 ** (length_number / 2)

                memoSplit[rocks_array[i]] = (left_part, right_part)

            rocks_array[i] = left_part
            rocks_array.append(right_part)

        else:
            if rocks_array[i] in memoMult:
                rocks_array[i] = memoMult[rocks_array[i]]

            else:
                multiplied_number = rocks_array[i] * 2024
                memoMult[rocks_array[i]] = multiplied_number

                rocks_array[i] = multiplied_number

        i += 1

    print(i)

print(len(rocks_array))
