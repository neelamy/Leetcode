# Source : https://leetcode.com/problems/rotate-array/description/

# Algo/DS : Array

# Complexity : O(n)


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums[:] = nums[len(nums) - k:] + nums[0: len(nums) - k]
       
