
# Source : https://leetcode.com/submissions/detail/127017584/
# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

# Algo/DS : Array

# Complexity : O(n^2)

class Solution(object):
    def setZeroes(self, matrix):
        
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        row = len(matrix)
        col = len(matrix[0])
        
        flag = False
        for i in range(row):
            for j in range(col):              
                if matrix[i][j] == 0:
                    flag = True
                    matrix[i][j] = "N"
            if flag:
                for k in range(col):
                        matrix[i][k] = 0 if matrix[i][k]!= "N" else "N"                
            flag = False
            
                    
        for i in range(col):
            for j in range(row):   
                if matrix[j][i] == "N":
                    for k in range(row):
                        matrix[k][i] = 0
                       