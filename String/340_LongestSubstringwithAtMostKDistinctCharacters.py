# Source : https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/description/

# Algo/DS : Sliding window, string

# Complexity : O(n)


class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        d = {}
        
        start, end = 0,0
        max_length = 0
        
        for i in range(len(s)):
            d[s[i]] = d.get(s[i], 0) + 1
           # print d
            if len(d.keys()) > k:
                d[s[start]] -= 1
                if  d[s[start]] == 0 : del  d[s[start]]
                start += 1
            max_length = max(max_length, i - start + 1)
                
        return max_length