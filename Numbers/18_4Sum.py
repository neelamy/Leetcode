# Source : https://leetcode.com/problems/4sum/description/

# Algo/DS : Number

# Complexity : 

from collections import defaultdict
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
    
        ans ={}
        d= defaultdict(list)
        n = len(nums) 
        for i in xrange(n):
            for j in xrange(n):
                if i != j and  i < n:
                    d[nums[i] + nums[j]].append([i,j])
                    
        for i in d:
            if  target -i in d:
                for l1 in d[i]:
                    for l2 in d[target -i]:
                        if l1[0] not in l2 and l1[1] not in l2 and l2[0] not in l1 and l2[1] not in l1:
                           
                            ans[tuple(sorted([nums[l1[0]], nums[l1[1]], nums[l2[0]], nums[l2[1]]]))] = 1
                    
        return ans.keys()
        