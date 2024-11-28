# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
    

        area = 0

        i = 0
        j = len(height) - 1

        while True:
            first_ptr = height[i]
            last_ptr = height[j]

            smallest_side = min(first_ptr,last_ptr)
            distance = j - i 
            temp_area = smallest_side * distance
            if temp_area > area:
                area = temp_area
        
            if smallest_side == last_ptr:
                j = j - 1
            else:
                i =  i + 1
           
            if distance <= 0:
                return area
