# Source : https://leetcode.com/problems/word-break-ii/description/

# Algo/DS : Graph, DFS

# Complexity : O()

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        wordDict = set(wordDict)
        d = {}        
        return self.check( s,wordDict, d)

        
    def check(self,s,wordDict, d):
        # if s has been processed then return its result
        if s in d: 
            return d[s]
        # return empty list if not s
        if not s :     
            return []    
        res = []
        for i in range(len(s)):

            # check all possible prefix of s
            if s[:i+1] in wordDict:

                # if prefix in wordDict and no remanining char left then
                # append it to dict
                if i == len(s) -1: res.append(s[:i+1])
                else:
                    
                    # else get the result of remaining chars
                    remaining = self.check( s[i+1:],wordDict, d)

                    # append current word to each result
                    for string in remaining:
                        string = s[:i+1] + " " + string
                        res.append(string)

        # update dict
        d[s] = res
        return res
            
                