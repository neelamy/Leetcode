# Source : https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/description/

# Algo/DS : String, recursion

# Complexity : O(n), space = O(1)

from collections import Counter
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s: return 0
        if k> len(s) : return 0

        # get each char of string
        for char in set(s):

            # find 1st char which has count < k and then split on that char
            if s.count(char)< k : return max(self.longestSubstring(t, k) for t in s.split(char))
        
        # no char has count < k so return the entire length    
        return len(s)
        