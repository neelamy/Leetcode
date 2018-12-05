# Source : https://leetcode.com/problems/minimum-window-substring/description/

# Algo/DS : Sliding window, string

# Complexity : O(n)

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        result = []
        
        pattern = {}
        string = {}
        
        # create freq count for pattern
        for char in t:
            pattern[char] = pattern.get(char, 0) + 1
            
        start, end = 0,0
        pattern_length = len(t)
        string_length = len(s)    
        count = 0
        min_length = string_length
        final_start = -1
        # start loop
        while end < string_length:

            # create freq count for string
            string[s[end]] = string.get(s[end], 0) + 1

            # increment count only if char is needed and its freq is low or equal
            if s[end] in pattern and string[s[end]] <= pattern[s[end]]: count += 1
            
            # once freq count matches pattern length
            if count == pattern_length:

                # move start to remove unnecessary char
                ## if char at start is not in pattern or its number of occurance is more than pattern
                # move start to next char and reduce the count of that char in string dict
                while s[start] not in pattern  or string[s[start]] > pattern[s[start]] : 
                    string[s[start]] -= 1
                    start += 1

                # once start is fixed, if length is less than min length
                if end - start + 1 <= min_length: 
                    min_length = end - start + 1
                    final_start = start

                                
            end += 1
            
                
            
        
        return s[final_start: final_start + min_length ]
    