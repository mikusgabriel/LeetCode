# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
    
        list=[]
        for char in s:
            if char in ("(", "{", "["):
                list.append(char)
            else:
                if len(list) == 0:
                    return False
                counter=0
                for value in reversed(list):
                    counter+=1
                    if len(value)==1 :
                        if value== chr(ord(char) - self.getASCII(char)):
                            list[len(list)-counter]=value+char
                            break
                                
                        else:
                            return False    
                   
          
        for value in list:
            if len(value) != 2:
                return False
            
        
        return True

    def getASCII(self,char):
        if char == ')':
            return 1
        else:
            return 2
        
        

# .______    _______ .___________.___________. _______ .______         ____    __    ____  ___   ____    ____ 
# |   _  \  |   ____||           |           ||   ____||   _  \        \   \  /  \  /   / /   \  \   \  /   / 
# |  |_)  | |  |__   `---|  |----`---|  |----`|  |__   |  |_)  |        \   \/    \/   / /  ^  \  \   \/   /  
# |   _  <  |   __|      |  |        |  |     |   __|  |      /          \            / /  /_\  \  \_    _/   
# |  |_)  | |  |____     |  |        |  |     |  |____ |  |\  \----.      \    /\    / /  _____  \   |  |     
# |______/  |_______|    |__|        |__|     |_______|| _| `._____|       \__/  \__/ /__/     \__\  |__|     
                                                                                                            
       
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        # Dictionary to hold matching pairs
        matching_bracket = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in matching_bracket.values():
                # If the character is one of the opening brackets, push it onto the stack
                stack.append(char)
            elif char in matching_bracket.keys():
                # If the character is one of the closing brackets, check for the corresponding opening bracket
                if stack == [] or matching_bracket[char] != stack.pop():
                    return False
            else:
                # If the character is not a bracket, continue (optional, depends on problem constraints)
                continue

        # If the stack is empty, all the opening brackets were properly closed
        return stack == []
