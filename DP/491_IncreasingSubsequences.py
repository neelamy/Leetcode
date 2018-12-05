
# Source : https://leetcode.com/problems/increasing-subsequences/description/

# Algo/DS : Array, DP, LIS

# Complexity : O(n^2 * k) k = length of largest array set

class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        # perform normal LIS and instead of increasing count
        # here we add it to previous element's array result
        res = [[[i]] for i in nums]
        for i in range(len(nums)):
            for j in range(0,i):
                if nums[j] <= nums[i]:
                    for k in res[j]:
                        res[i].append(k+[nums[i]])
                                      
        s =set()
        
        # get all array with length >= 2. Use set to avoid duplicates
        for i in res:
            for j in i:
                if len(j) >=2: s.add(tuple(j))
                    
        return list(s)
        