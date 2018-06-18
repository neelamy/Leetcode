
# Source : https://leetcode.com/problems/3sum/description/

# Algo/DS : Array

# Complexity : O(n^2)


from collections import defaultdict
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # pair would be stored in dict as key to avoid duplication
        res = {}       
        n = len(nums)

        # important step is to sort before hand
        nums = sorted(nums)
        
        for i in xrange(n-1):
            j = i + 1
            k = n-1   

            # this is needed to handle the case like[0,0,0,0,0,0,0,0,0...........]
            # else it would be TLE  
            if i > 1 and nums[i] == nums[i-1]:
                continue 

            while(j < k):
                if nums[i] + nums[j] + nums[k] == 0:
                    res[(nums[i], nums[j] , nums[k])] = 1
                if nums[i] + nums[j] + nums[k] > 0:
                    k = k -1
                else: j = j + 1
                    
        return res.keys()
                
        
        
        
       