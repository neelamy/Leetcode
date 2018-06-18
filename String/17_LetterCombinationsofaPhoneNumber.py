
# Source : https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

# Algo/DS : Array

# Complexity : O(n + m)

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d = {'2': "abc",'3': "def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':'tuv', '9': 'wxyz'}
        
        # perform DFS
        result = []
        if digits == "": return result
        current_number = digits[0]
        postfix = self.letterCombinations(digits[1:])
        for cur_letter in d[current_number]:
            if postfix != []:
                for s in postfix:
                    result.append(cur_letter + s)
            else:
                result.append(cur_letter)
             
        return result
        
        