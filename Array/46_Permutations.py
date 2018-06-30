# Source : https://leetcode.com/problems/permutations/description/

# Algo/DS : Array

# Complexity : O(n*n!) path length = n, total path = n!

class Solution(object):

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        # return list so that it can be appended else it would give error
        # when there will be only 1 item
        if len(nums) == 1 : return [nums]

        perm = []
        for i in range(len(nums)):

        	# take all combinations : eg for [1,2,3], remainder would be
        	# [2,3], [1,3], [1,2]
            remainder = nums[0:i] + nums[i+1:]

            # call funtion on remainder
            suffix = self.permute(remainder)	

            # append the char to each item in suffix
            for suffix_item in suffix:
                perm.append([nums[i]] + suffix_item)


        return perm

