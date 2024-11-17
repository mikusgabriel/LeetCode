
# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

 

# Example 1:

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
# Example 2:

# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].
# Example 3:

# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        if len(digits) == 0 :
           digits[0] = digits[0] + 1
           return digits
        

        digits.reverse()
        
        digits = self.increment(digits, 0)
        print(digits)
        digits.reverse()
        print(digits)

        return digits

    def increment(self, tab, n):
        if n >= len(tab):
            tab.append(1)
            return tab
        if tab[n] == 9:
            tab[n] = 0
            return self.increment(tab, n + 1)
        else:
            tab[n] = tab[n] + 1
            return tab
            
        
# beat 100% in speed
