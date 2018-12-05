# Source : https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

# Algo/DS : Sliding window, string

# Complexity : O(n)

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        result = []
        
        pattern = {}
        string = {}
        
        # create freq count for pattern
        for char in p:
            pattern[char] = pattern.get(char, 0) + 1
            
        start, end = 0,0
        pattern_length = len(p)
        string_length = len(s)    
        count = 0
        
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

                # once start is fixed, check if start to end is same as pattern length
                # if it is then save start in result
                # move start again so that next occurance of pattern can be found
                # reduce count and freq of start in dict
                if end - start + 1 == pattern_length: 
                    result.append(start)
                    string[s[start]] -= 1
                    start += 1
                    count -=1
                                
            end += 1
            
                
            
        
        return result
    