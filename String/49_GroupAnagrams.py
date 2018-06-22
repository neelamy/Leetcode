# Source : https://leetcode.com/problems/group-anagrams/description/

# Algo/DS : String

# Complexity : O(n (Klogk)) where k is length of longest string and n
# is number of strings

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}       
        for word in strs:
            key = "".join(sorted(word))
            d[key] = d.get(key,[]) + [word]   
        return d.values()
    
        