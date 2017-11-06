# Source :https://leetcode.com/problems/ransom-note/description/

# Algo/DS : Strings

# Complexity : O(n)

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dransome = {}
        for i in ransomNote:
            dransome[i] = dransome.get(i,0) + 1          
        dmagazine = {}
        for i in magazine:
            dmagazine[i] = dmagazine.get(i,0) + 1         
        for i in dransome:
            if i not in dmagazine or dransome[i] > dmagazine[i] : return False          
        return True
