# 75. Sort Colors
# Solved
# Medium
# Topics
# Companies
# Hint
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

 

# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]
 









class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # selection sort
        ptr=0
        
        
        for i in range(len(nums)):
            ptr = i
            second_ptr = i
            smallest = nums[i]
            temp = smallest
            for j in range(i,len(nums)):
                temp_smallest = nums[j]
                if smallest > temp_smallest:
                    smallest = temp_smallest
                    second_ptr = j

            nums[ptr] = smallest
            nums[second_ptr] = temp

        

# slow as hell but works for arrays with more cases than only {0,1,2} 
