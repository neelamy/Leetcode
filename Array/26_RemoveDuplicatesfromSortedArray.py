# Source : https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

# Algo/DS : Array

# Complexity :O(n)

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if  nums == [] or len(nums) == 1: return len(nums)
        ptr , current = 1, 1
        while current < len(nums):
            if nums[current] != nums[current - 1]:
                nums[ptr] = nums[current]
                ptr += 1
                current += 1
            else:
                current += 1
                
        return ptr 