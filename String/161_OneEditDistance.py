# Source : https://leetcode.com/problems/one-edit-distance/description/

# Algo/DS : DP

# Complexity :

class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if abs(len(s) - len(t)) > 1: return False
    
        count = 0
        t_i , s_j = 0,0
        while t_i <len(t) and s_j < len(s):
            if s[s_j] == t[t_i] : 
                t_i += 1
                s_j += 1
                continue
            if count : return False
            else:
                count += 1
                if len(s) >= len(t) : s_j += 1
                if len(s) <= len(t):
                    t_i += 1
                
        count += len(s[s_j:]) + len(t[t_i:])
                
        return  count == 1 
        