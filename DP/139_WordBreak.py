
# Source : https://leetcode.com/problems/word-break/description/

# Algo/DS : Array, DP

# Complexity : O(n^2)

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        dp =[False] * len(s)
        wordDict = set(wordDict)
        
        for i in range(len(s)):
            if s[0:i+1] in wordDict:
                dp[i] = True
            if dp[i]:
                for j in range(i + 1 , len(s)):
                    if s[i+1:j + 1] in wordDict:
                        dp[j] = True
                    if dp[-1] == True : return True
        print dp           
        return dp[-1] == True
                    
