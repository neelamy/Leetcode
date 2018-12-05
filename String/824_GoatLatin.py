# Source : https://leetcode.com/problems/goat-latin/description/

# Algo/DS : string

# Complexity : O(n)

class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        
        S = S.split()
        
        temp = ""
        
        for index, word in enumerate(S):
            if word[0] in ['a','A','i','I','o','O','u','U','e','E']:
                word = word + 'ma'
            else:
                 word = word[1:] + word[0] + 'ma'
                 
            word = word + "a"*(index + 1)
            
            temp += word + " "
            
        
        return temp.strip()
                