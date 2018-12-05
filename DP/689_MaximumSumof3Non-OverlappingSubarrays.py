
# Source : https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/description/

# Algo/DS : Array DP

# Complexity : O(n) n = no of digits

#Explanation: https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/solution/

class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        # create sum of window. W[i] will have sum of window k when window starts at i
        W = []
        W.append(sum(nums[:k]))   
        for index, n in enumerate(nums[k:]):            
            total = W[-1] + n - nums[index]
            W.append(total)
        

        left, right = [0]* len(W),  [0]* len(W)
        
        # find each window find index of best left window 
        # since it has to be lexicographically smaller hence use > and not >=
        best = 0
        for i in range(len(W)):
            if W[i]> W[best]: best = i
            left[i] = best
         
        # find each window find index of best right window   
        best = len(W)-1
        for i in range(len(W)-1, -1, -1):
            if W[i]> W[best]: best = i
            right[i] = best
            
        
        # initialize ans
        ans = [-1,-1,-1]

        # now we have to select middle window
        # since windows have to be non overlapping, j will start from k
        # because W[k] will be first non overlappnig window
        # and last overlapping window will be len(W)-k -1
        for j in range(k, len(W)-k ):

            # left window will start at j-k
            # so select best left window for that location
            i = left[j - k]

            # for j, select best right window for that location
            r = right[j +k]
            
            # check if they give better result
            if ans[0]== -1 or( W[ans[0]]+W[ans[1]]+W[ans[2]] < W[i]+W[j]+W[r]):
                ans[0]= i
                ans[1]= j
                ans[2]= r
                
        return ans
            
            
            
            
            
            
            
          