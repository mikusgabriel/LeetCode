// 329. Longest Increasing Path in a Matrix

// Given an m x n integers matrix, return the length of the longest increasing path in matrix.

// From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

// Example 1:

// Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
// Output: 4
// Explanation: The longest increasing path is [1, 2, 6, 9].
// Example 2:

// Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
// Output: 4
// Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
// Example 3:

// Input: matrix = [[1]]
// Output: 1

#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

class Solution
{
public:
    int longestIncreasingPath(std::vector<std::vector<int>> &matrix)
    {

        if (matrix.empty())
            return 0;

        int lenght = matrix.size();
        int width = matrix[0].size();

        std::vector<std::vector<int>> memo(lenght, std::vector<int>(width, 0));

        int longestPath = 0;
        for (int i = 0; i < lenght; i++)
        {
            for (int j = 0; j < width; j++)
            {

                std::set<std::pair<int, int>> set;
                set.insert({i, j});
                int temp = findLongestIncreasingPath(i, j, 1, set, lenght, width, matrix, memo);

                if (temp > longestPath)
                {
                    longestPath = temp;
                }
            }
        }

        return longestPath;
    }

    int findLongestIncreasingPath(int i, int j, int cmp, std::set<std::pair<int, int>> &set, int lenght, int width, std::vector<std::vector<int>> &matrix, std::vector<std::vector<int>> &memo)
    {

        if (memo[i][j] != 0)
            return memo[i][j];

        std::vector<std::vector<int>> possibility = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

        set.insert({i, j});

        int max = 1;

        for (std::vector<int> list : possibility)
        {

            int new_i = i + list[0];
            int new_j = j + list[1];

            if (!set.count({new_i, new_j}) && inBounds(new_i, new_j, lenght, width) && matrix[i][j] < matrix[new_i][new_j])
            {
                // std::cout << new_i << ", " << new_j << "\n";

                max = std::max(1 + findLongestIncreasingPath(new_i, new_j, ++cmp, set, lenght, width, matrix, memo), max);
            }
        }
        // std::cout << max << "\n";

        set.erase({i, j});
        memo[i][j] = max;

        return max;
    }

    bool inBounds(int i, int j, int length, int width)
    {

        if (i < 0 || i >= length)
        {
            return false;
        }
        else if (j < 0 || j >= width)
        {
            return false;
        }
        return true;
    }
};

int main()
{

    Solution sol = Solution();

    std::vector<std::vector<int>> matrix = {
        {0, 1, 2, 3, 4, 5, 6, 7, 8, 9},
        {19, 18, 17, 16, 15, 14, 13, 12, 11, 10},
        {20, 21, 22, 23, 24, 25, 26, 27, 28, 29},
        {39, 38, 37, 36, 35, 34, 33, 32, 31, 30},
        {40, 41, 42, 43, 44, 45, 46, 47, 48, 49},
        {59, 58, 57, 56, 55, 54, 53, 52, 51, 50},
        {60, 61, 62, 63, 64, 65, 66, 67, 68, 69},
        {79, 78, 77, 76, 75, 74, 73, 72, 71, 70},
        {80, 81, 82, 83, 84, 85, 86, 87, 88, 89},
        {99, 98, 97, 96, 95, 94, 93, 92, 91, 90},
        {100, 101, 102, 103, 104, 105, 106, 107, 108, 109},
        {119, 118, 117, 116, 115, 114, 113, 112, 111, 110},
        {120, 121, 122, 123, 124, 125, 126, 127, 128, 129},
        {139, 138, 137, 136, 135, 134, 133, 132, 131, 130},
        {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}};

    // Expected Output: 9 (Path: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9)

    std::cout << sol.longestIncreasingPath(matrix);

    return 0;
}
