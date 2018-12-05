# Source : https://leetcode.com/problems/n-queens/description/

# Algo/DS : DFS, n queen

# Complexity : O(n!)


class Solution(object):
    
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.n = n
        self.matrix = [["."] * n for i in range(n)]
        self.result = []
        self.dfs(0)
        return self.result
    
    def dfs(self, col):
        if col >= self.n : 
            mat = ["".join(current_row) for current_row in self.matrix]
            self.result.append(mat)
        
        for i in range(self.n):
            if self.issafe(i, col):
                self.matrix[i][col] = "Q"
                self.dfs(col + 1)
                self.matrix[i][col] = "."

                
    def issafe(self, row, col):
        
        for r in range(self.n):
            for c in range(col):
                                                # same row    bottom left dig     upper left dig
                if self.matrix[r][c] == 'Q' and (row == r or r+c == row+ col or r-c == row - col): return False
            
        return True