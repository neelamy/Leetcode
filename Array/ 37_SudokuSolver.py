# Source : https://leetcode.com/problems/sudoku-solver/description/

# Algo/DS : Array, Bactracking

# Complexity : 

class Solution(object):
    
    def check(self, board, i,j,val):
        cells = [[0,1,2],[3,4,5],[6,7,8]]
        for cell in cells:
            if i in cell: row = cell
            if j in cell: col = cell
        if val in board[i] : return False 
        for x in range(9) : 
            if board[x][j] == val: return False         
        count = 0
        for i_cell in row:
            for j_cell in col:
                if val == board[i_cell][j_cell] : return False
        return True
 
    def update_board(self, board, i, j):
        if i == 9 : return True
        if j == 9  : return (self.update_board(board, i + 1, 0))
               
        if board[i][j] != "." :  return (self.update_board(board, i, j + 1))
        numbers = map(str,range(1, 10))                    
        for number in numbers: 
            if self.check(board, i, j, number) :     
                board[i][j] = number
                if self.update_board(board, i, j + 1) :return True
                board[i][j] = "."
        return False
                
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        
        self.update_board(board, 0,0)
       
        
          
                    
                
                
        