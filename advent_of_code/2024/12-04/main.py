f = open("data.txt", "r")
arr = f.read().split("\n")

for i in arr:
    i.split()
arr = arr[:-1]


def first_test(arr):
    summ = 0

    for i in range(len(arr)):
        # columns
        for j in range(len(arr[i])):
            word_row = ""
            word_col = ""
            word_top_right_diago = ""
            word_top_left_diago = ""
            for k in range(0, 4):
                # check rows

                if j <= len(arr[i]) - 4:
                    # always going LEFT to RIGHT since the others before already have searched!

                    word_row += arr[i][j + k]
                    if (
                        k >= 3
                        and len(word_row) == 4
                        and (word_row == "XMAS" or word_row == "SAMX")
                    ):
                        print("found a word row", word_row)
                        summ += 1

                # check columns
                if i <= len(arr) - 4:
                    # always going HIGH to LOW since the others before already have searched!

                    word_col += arr[i + k][j]

                    if (
                        k >= 3
                        and len(word_col) == 4
                        and (word_col == "XMAS" or word_col == "SAMX")
                    ):
                        print("found a word col", word_col)
                        summ += 1

                # check top right diagonals
                if j <= len(arr[i]) - 4 and i >= 3:
                    # always going LOW to HIGH and LEFT to RIGHT since the others before already have searched!

                    word_top_right_diago += arr[i - k][j + k]

                    if (
                        k >= 3
                        and len(word_top_right_diago) == 4
                        and (
                            word_top_right_diago == "XMAS"
                            or word_top_right_diago == "SAMX"
                        )
                    ):
                        print("found a word diago right", word_top_right_diago)
                        summ += 1

                # check top left diagonals
                if j >= 3 and i >= 3:
                    # always going LOW to HIGH and RIGHT to LEFT since the others before already have searched!

                    word_top_left_diago += arr[i - k][j - k]

                    if (
                        k >= 3
                        and len(word_top_left_diago) == 4
                        and (
                            word_top_left_diago == "XMAS"
                            or word_top_left_diago == "SAMX"
                        )
                    ):
                        print("found a word diago left", word_top_left_diago)
                        summ += 1

    print(summ)


first_test(arr)


def second_test(arr):
    summ = 0
    list_right_possible = []
    list_left_possible = []
    for i in range(len(arr)):
        # columns
        for j in range(len(arr[i])):
            word_top_right_diago = ""
            word_top_left_diago = ""
            for k in range(0, 3):
                # check top right diagonals
                if j <= len(arr[i]) - 3 and i >= 2:
                    word_top_right_diago += arr[i - k][j + k]

                    if (
                        k >= 2
                        and len(word_top_right_diago) == 3
                        and (
                            word_top_right_diago == "MAS"
                            or word_top_right_diago == "SAM"
                        )
                    ):
                        print("found a word diago right", word_top_right_diago)
                        list_right_possible.append((i - k + 1, j + k - 1))

                # check top left diagonals
                if j >= 2 and i >= 2:
                    word_top_left_diago += arr[i - k][j - k]

                    if (
                        k >= 2
                        and len(word_top_left_diago) == 3
                        and (
                            word_top_left_diago == "MAS" or word_top_left_diago == "SAM"
                        )
                    ):
                        print("found a word diago left", word_top_left_diago)
                        list_left_possible.append((i - k + 1, j - k + 1))

    for i in range(len(list_left_possible)):
        for j in range(len(list_right_possible)):
            if list_left_possible[i] == list_right_possible[j]:
                summ += 1

    print(summ)


second_test(arr)
