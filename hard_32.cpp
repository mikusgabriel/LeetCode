// 32. Longest Valid Parentheses
// Solved
// Hard
// Topics
// Companies
// Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses 
// substring
// .

 

// Example 1:

// Input: s = "(()"
// Output: 2
// Explanation: The longest valid parentheses substring is "()".
// Example 2:

// Input: s = ")()())"
// Output: 4
// Explanation: The longest valid parentheses substring is "()()".
// Example 3:

// Input: s = ""
// Output: 0




#include <iostream>
#include <stack>

class Solution
{
public:
    int longestValidParentheses(std::string s)
    {
        int biggestSub = 0;

        if (s.size() == 0)
        {
            return 0;
        }
        for (int i = 0; i < s.size() - 1; i++)
        {

            if (s[i] == '(')
            {
                std::stack<char> stack;
                std::cout << s[i];
                stack.push(s[i]);

                int tempSub = 1;
                for (int j = i + 1; j < s.size(); j++)
                {

                    std::cout << s[j];

                    if (!stack.empty() && stack.top() == '(' && s[j] == ')')
                    {
                        stack.pop();
                    }
                    else
                    {
                        stack.push(s[j]);
                    }

                    tempSub += 1;

                    if (stack.empty())
                    {
                        if (tempSub > biggestSub)
                        {
                            biggestSub = tempSub;
                        }
                    }
                }
            }
        }

        return biggestSub;
    }
};

int main(){

    Solution sol = Solution();

    std::string s1 = "(()())";      // ✅ Valid parentheses (Length: 6)
    std::string s2 = ")()())";      // ✅ Longest valid: "()()" (Length: 4)
    std::string s3 = "((()))";      // ✅ Fully valid (Length: 6)
    std::string s4 = "())";         // ✅ Longest valid: "()" (Length: 2)
    std::string s5 = "(()";         // ✅ Longest valid: "()" (Length: 2)
    std::string s6 = "";            // ✅ Edge case: Empty string (Length: 0)
    std::string s7 = "()(()";       // ✅ Longest valid: "()" (Length: 2)
    std::string s8 = "(()))())(";   // ✅ Longest valid: "(()))()" (Length: 6)
    std::string s9 = ")))(((";      // ❌ No valid substrings (Length: 0)
    std::string s10 = "()(())";     // ✅ Longest valid: "()(())" (Length: 6)

    // Debugging Output
    std::cout << "Test cases:\n";
    std::cout << "s1: " << sol.longestValidParentheses(s1) << "\n";
    std::cout << "s2: " << sol.longestValidParentheses(s2) << "\n";
    std::cout << "s3: " << sol.longestValidParentheses(s3) << "\n";
    std::cout << "s4: " << sol.longestValidParentheses(s4) << "\n";
    std::cout << "s5: " << sol.longestValidParentheses(s5) << "\n";
    std::cout << "s6: " << sol.longestValidParentheses(s6) << "\n";
    std::cout << "s7: " << sol.longestValidParentheses(s7) << "\n";
    std::cout << "s8: " << sol.longestValidParentheses(s8) << "\n";
    std::cout << "s9: " << sol.longestValidParentheses(s9) << "\n";
    std::cout << "s10: " << sol.longestValidParentheses(s10) << "\n";
    return 0;
}
