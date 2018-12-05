# Source : https://leetcode.com/problems/valid-number/description/

# Algo/DS : valid number

# Complexity : O(n)
'''
If we see [0-9] we set the number flags.
We can only see . if we didn't see e or ..
We can only see e if we didn't see e but we did see a number. We reset number flag.
We can only see + and - in the beginning and after an e
any other character break the validation.
At the and it is only valid if there was at least 1 number and if we did see an e then a number after it as well.
'''

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        if not s : return False
        e = False
        dot = False
        number = False
        for i in range(len(s)):
            if i == 0 and s[i] in ['+', '-']: continue
            if s[i].isdigit(): 
                number = True
                continue
            if s[i] == 'e':
                if e or not number: return False
                e = True
                number = False
            elif s[i] =='.':
                if e or dot: return False
                dot = True
            elif s[i] in ['+', '-']:
                if s[i-1] != 'e': return False
            else:
                return False
        return True if number else False
            
        