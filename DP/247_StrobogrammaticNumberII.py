# Source : https://leetcode.com/problems/strobogrammatic-number-ii/description/

# Algo/DS : DP, string

# Complexity : O(n)

class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return self.helper(n, True)
        
        
    def helper(self, n ,isouter):
        
        # return list not "" else for 2 it will fail
        if  n == 0: return [""]
        if n == 1: return ["1", "8", "0"]
        
        # we add no of left and right so find list for n-2
        middle_list = self.helper(n-2, False)
        res = []

        # take the middle list and append no on left and right
        # add 0 only if its part of inner list
        for s in middle_list:
            if not isouter:
                res.append("0" + s + "0") 
            res.append("1" + s + "1")
            res.append("8" + s + "8")
            res.append("6" + s + "9")
            res.append("9" + s + "6")
        return res
                
        