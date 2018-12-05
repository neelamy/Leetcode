# Source : https://leetcode.com/problems/permutation-in-string/description

# Algo/DS : Sliding window, string

# Complexity : O(n)

from collections import Counter
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        d_s1 = Counter(s1)
        d_s2 = {}
        
        start = 0
        count = 0
        
        for index, char in enumerate(s2):
            d_s2[char] = d_s2.get(char, 0) + 1
            
            if char in d_s1 and d_s2[char] <= d_s1[char]: 
                count += 1
                         
            if count == len(s1):
                while s2[start] not in d_s1 or d_s2[s2[start]] > d_s1[s2[start]]:
        
                        d_s2[s2[start]] -=1
                        
                        start += 1
        
                if index - start + 1 == len(s1):
                    return True
        
        return False
                        
            
            
        