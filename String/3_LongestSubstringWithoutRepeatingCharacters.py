# Source : https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

# Algo/DS : String

# Complexity : O(n)


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """    
        max_len =  0 
        d ={}
        start = -1 
        for index,char in enumerate(s):
            if char in d :
                start = max(start, d[char])
            d[char] = index
            max_len = max(max_len, index - start)               
        return max_len
                