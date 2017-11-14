
# Source : https://leetcode.com/problems/majority-element/description/

# Algo/DS : Array

# Complexity : O(n*n)


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        
        res = [[0 for j in range(n)] for i in range(n)]
        
        row_start = 0; col_start = 0; count = 1
        row_last = n-1 ; col_last = n-1
        
        while row_start <= row_last and col_start <= col_last :
            
            for t in range(col_start, col_last + 1):
                res[row_start][t] = count      
                count += 1
                
            row_start += 1
           
             
            for t in range(row_start, row_last + 1):
                res[t][col_last] = count      
                count += 1
                
            col_last -=1
           
            for t in range(col_last , col_start - 1, -1):
                res[row_last][t] = count      
                count += 1
                
            row_last -= 1
            
            for t in range(row_last, row_start - 1, -1):
                res[t][col_start] = count      
                count += 1
                
            col_start +=1
        
        return res
            