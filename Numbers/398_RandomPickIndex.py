
# Source : https://leetcode.com/problems/random-pick-index/description/

# Algo/DS : Random number

# Complexity : O(n)

import random
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        count = 0
        index = -1
        for i in range(len(self.nums)):

            # if number not same as target then skip
            if self.nums[i] != target: continue
            
            # increament count
            count += 1

            # target occurs count time. So pick a random number between 1 to count
            # probability of getting 1 = 1/count
            # so if its 1 select that index
            if random.randint(1,count) == 1:
                index = i
        
        # return index   
        return index
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)