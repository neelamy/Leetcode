
# Source : https://leetcode.com/problems/3sum/description/

# Algo/DS : Array

# Complexity : O(n^2)

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # important step is to sort before hand
        nums.sort()
        m = float("inf") 
        ans = 0
        n = len(nums)
        for i in xrange(n - 1):
            j = i + 1
            k = n - 1
            # this is needed to handle the case like[0,0,0,0,0,0,0,0,0...........]
            # else it would be TLE 
            if i > 1 and nums[i] == nums[i-1]: continue
            
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                dist = abs(target - total)
                if dist == 0 : return total
                if dist < m:
                    m = dist
                    ans = total
                if total > target:
                    k -= 1
                else: j += 1
                
               
        return ans
    
    
    