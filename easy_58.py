# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal 
# substring
#  consisting of non-space characters only.

 

# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:

# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.



#First Try, suboptimal? 33% speed 30% memory

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split()[-1])
        
        
#Second Try, better 55% speed 13% memory

class Solution(object):  
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = 0

        if len(s) == 1:
            return 1

        for i in range(len(s),0,-1):

            if s[i-1] != ' ':
                
                counter = counter + 1
                 
                if i==1 or s[i-2] == ' ':
                    return counter

        return 0
