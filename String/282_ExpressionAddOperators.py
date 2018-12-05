'''
# Source : https://leetcode.com/problems/expression-add-operators/description/

# Algo/DS : recursion, string, dfs

# Complexity : O(4^n)
The process moving to N length of string gives us from 3T(n-1) to 3T(1) :
T(n) = 3 * T(n-1) + 3 * T(n-2) + 3 * T(n-3) + ... + 3 *T(1);
T(n-1) = 3 * T(n-2) + 3 * T(n-3) + ... 3 * T(1);
Thus T(n) = 4T(n-1);

'''


class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        
        if num == "": return []   
        res = []       
        self.dfs(res, num,target,"", 0, 0)      
        return res
    
    
    
    def dfs(self, res, remain, target, path,current_total, last_value):
        if remain == "" and target == current_total: 
            res.append(path)
            return res
        for i in range(len(remain)):

            # if length of string > 1 and string starts with '0' like '05' then break as 
            # this string is not valid
            if i> 0 and  remain[0] == '0':break

            # take left(including i) and right(from i+1)
            left, right = remain[:i+1], remain[i+1:]

            # change left to int
            left = int(left)

            # if no path that means its first char so just add it and call dfs
            if not path :
                self.dfs(res, right,target,path + str(left),current_total+ left,  left)
            else:
                # else add +,*,-
                # last value store previous operand which is required in case of multiplication
                # eg (3+2*3) here we need 2 so that we can do 5 - 2 + 6 ie. (3+2) - 2 +(2*3)
                self.dfs(res, right,target ,path +"+" + str(left),current_total+ left, left)
                self.dfs(res, right,target ,path + "-"+ str(left),current_total- left, -left)
                self.dfs(res, right,target ,path + "*"+str(left), current_total-last_value +(last_value* left),last_value* left)
                
        return res
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                
        
        
        
        
        