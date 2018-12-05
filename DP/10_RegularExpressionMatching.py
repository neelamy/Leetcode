
# Source : https://leetcode.com/problems/regular-expression-matching/description/

# Algo/DS : DP, regular expression

# Complexity : O(n*m)

#Explanation: https://leetcode.com/problems/regular-expression-matching/discuss/161365/Java-solution-with-more-detailed-explanation
'''

1, If p.charAt(j) == s.charAt(i) :  dp[i][j] = dp[i-1][j-1];
2, If p.charAt(j) == '.' : dp[i][j] = dp[i-1][j-1];
3, If p.charAt(j) == '*': 
   here are two sub conditions:
               1   if p.charAt(j-1) != s.charAt(i) : dp[i][j] = dp[i][j-2]  //in this case, a* only counts as empty
               2   if p.charAt(i-1) == s.charAt(i) or p.charAt(i-1) == '.':
                              dp[i][j] = dp[i-1][j]    //in this case, a* counts as multiple a 
                           or dp[i][j] = dp[i][j-1]   // in this case, a* counts as single a
                           or dp[i][j] = dp[i][j-2]   // in this case, a* counts as empty
'''
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        dp = [[False for j in range(len(p)+ 1)] for i in range(len(s)+ 1)]
        dp[0][0] = True
        
        for i in range(1, len(p)+ 1):
            if p[i-1] == "*": dp[0][i] = dp[0][i-2]
    
        for i in range(1, len(s)+ 1):
            for j in range(1, len(p)+ 1):
                
                if s[i-1] == p[j-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                if p[j-1] =='*':
                    if s[i-1] != p[j-2] and p[j-2] != '.': dp[i][j] = dp[i][j-2]
                    else:
                        dp[i][j] = dp[i-1][j] or dp[i][j-2] #or dp[i][j-1]
                        
        return dp[-1][-1]
 
        