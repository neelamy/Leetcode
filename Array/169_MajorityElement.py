
# Source : https://leetcode.com/problems/majority-element/description/

# Algo/DS : Array

# Complexity : O(n), Space: O(1)

class Solution(object):
    
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 1
        n = nums[0]
        for i in nums[1:]:
            if i == n : count += 1
            elif i != n :
                count -=1
                if count == 0:
                    count = 1
                    n = i
        return n