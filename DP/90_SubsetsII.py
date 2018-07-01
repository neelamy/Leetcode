# Source : https://leetcode.com/problems/subsets/description/

# Algo/DS : DP

# Complexity : O(n ^2)


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """


        result = [[]]
        nums.sort()
        
        for index,number in enumerate(nums):

        	# in case of duplicate number just add to list created by last number
        	# if number is not duplicate then take the current result length
        	# for duplicate data this value isnt changed and we take all elements
        	# from result after this value
            if index == 0 or number != nums[index - 1]:

                old_list_length = len(result)
            result += [ current + [number] for current in result[len(result) - old_list_length:]]
            
        return result