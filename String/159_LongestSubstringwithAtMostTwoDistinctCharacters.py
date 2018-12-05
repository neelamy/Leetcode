# Source : https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/description/

# Algo/DS : Sliding window, string

# Complexity : O(n)

class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        d = {}
        
        start, end = 0,0
        max_length = 0
        
        for i in range(len(s)):
            d[s[i]] = d.get(s[i], 0) + 1

            # if more than 2 chars then move start
            while len(d.keys()) > 2:
                d[s[start]] -= 1
                if  d[s[start]] == 0 : del  d[s[start]]
                start += 1
            max_length = max(max_length, i - start + 1)
                
        return max_length
