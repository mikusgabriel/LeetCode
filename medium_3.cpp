// 3. Longest Substring Without Repeating Characters
// Solved
// Medium
// Topics
// Companies
// Hint
// Given a string s, find the length of the longest 
// substring
//  without repeating characters.

 

// Example 1:

// Input: s = "abcabcbb"
// Output: 3
// Explanation: The answer is "abc", with the length of 3.
// Example 2:

// Input: s = "bbbbb"
// Output: 1
// Explanation: The answer is "b", with the length of 1.
// Example 3:

// Input: s = "pwwkew"
// Output: 3
// Explanation: The answer is "wke", with the length of 3.
// Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 




#include <string>
#include <iostream>
#include <map>

class Solution
{
public:
    int lengthOfLongestSubstring(std::string s)
    {

        // sliding window, wtoring in set, whern find a double, we starta giain from the index of the first item in the match fiykykyk
        int j = 0;
        std::map<char, int> subsequence;
        int longestSub = 0;
        for (int i = 0; i < s.size(); i++)
        {

            // if not in set
            if (subsequence.find(s[i]) == subsequence.end())
            {
                subsequence[s[i]] = i;
            }
            else
            {

                int difference = i - j;

                if (difference > longestSub)
                {
                    longestSub = difference;
                }
                int new_j = subsequence[s[i]] + 1;

                for (int k = j; k < new_j; k++)
                {
                    subsequence.erase(s[k]);
                }
                subsequence[s[i]] = i;
                j = new_j;
            }
        }

        if (s.size() - j > longestSub)
        {
            longestSub = s.size() - j;
        }

        return longestSub;
    }
};

int main()
{

    Solution sol = Solution();

    std::cout << sol.lengthOfLongestSubstring("abcabcbb") << std::endl; // Output: 3
    std::cout << sol.lengthOfLongestSubstring("bbbbb") << std::endl;    // Output: 1
    std::cout << sol.lengthOfLongestSubstring("pwwkew") << std::endl;   // Output: 3
    std::cout << sol.lengthOfLongestSubstring("abcdef") << std::endl;   // Output: 6
    std::cout << sol.lengthOfLongestSubstring("abba") << std::endl;     // Output: 2

    return 0;
}
