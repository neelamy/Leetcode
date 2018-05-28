# Source : https://leetcode.com/problems/valid-sudoku/description/

# Algo/DS : Array

# Complexity : O(1)


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            a = [0] * 10
            for j in range(9):
                if board[i][j] == ".": continue 
                if a[int(board[i][j])]  != 0 : return False
                else: a[int(board[i][j])] = 1
            
        for j in range(9):
            a = [0] * 10
            for i in range(9):
                if board[i][j] == ".": continue 
                if a[int(board[i][j])]  != 0 : return False
                else: a[int(board[i][j])] = 1
                    
        for k in range(0,7 , 3)   :
            a = [0] * 10
            b = [0] * 10
            c = [0] * 10
            for i in range(k , 3 + k):
                
                for j in range(0 , 3):
                    if board[i][j] == ".": continue 
                    if a[int(board[i][j])]  != 0 : return False
                    else: a[int(board[i][j])] = 1
                for j in range(3 , 6):
                    if board[i][j] == ".": continue 
                    if b[int(board[i][j])]  != 0 : return False
                    else: b[int(board[i][j])] = 1
                for j in range(6 , 9):
                    if board[i][j] == ".": continue 
                    if c[int(board[i][j])]  != 0 : return False
                    else: c[int(board[i][j])] = 1
       
                        
        
        return True
                        
                
        
            
        