class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        instanceOfNumber = {}
        k=0
        for number in nums:
            if not instanceOfNumber.get(number):
                instanceOfNumber[number] = True
                nums[k]=number
                k+=1

        return k
