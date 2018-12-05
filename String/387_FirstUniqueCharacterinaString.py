# Source : https://leetcode.com/problems/minimum-size-subarray-sum/description/

# Algo/DS : String

# Complexity : O(n) 


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        d= {}
        
        for i in s:
            d[i] = d.get(i, 0) + 1
        
        for index , char in enumerate(s):
            if d[char] == 1 : return index
            
        return -1