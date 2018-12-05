# Source : https://leetcode.com/problems/longest-common-prefix/description/

# Algo/DS : String

# Complexity :O(n*m) n = no of strings, m = length of smallest string

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ""
        first = strs[0]
        for index, char in enumerate(first):
            for other in strs[1:]:
                if len(other) <= index or other[index] != char :return first[:index]


        return first