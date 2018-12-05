# Source : https://leetcode.com/problems/wiggle-sort/description/

# Algo/DS : Sort, Array

# Complexity : O(n)

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        for i in range(1, len(nums),2):
            if i > 0 :
                if nums[i-1] > nums[i]: nums[i-1] , nums[i] =  nums[i] , nums[i-1]
            if i < len(nums) -1 :
                if nums[i + 1] > nums[i]: nums[i + 1] , nums[i] =  nums[i] , nums[i + 1]
