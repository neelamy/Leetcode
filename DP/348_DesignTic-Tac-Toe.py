# Source : https://leetcode.com/problems/design-tic-tac-toe/description/

# Algo/DS : Array, DP

# Complexity : O(1)

'''
Initially, I had not read the Hint in the question and came up with an O(n) solution. After reading the extremely helpful hint; a much easier approach became apparent. The key observation is that in order to win Tic-Tac-Toe you must have the entire row or column. Thus, we don't need to keep track of an entire n^2 board. We only need to keep a count for each row and column. If at any time a row or column matches the size of the board then that player has won.

To keep track of which player, I add one for Player1 and -1 for Player2. There are two additional variables to keep track of the count of the diagonals. Each time a player places a piece we just need to check the count of that row, column, diagonal and anti-diagonal.
'''

class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.row = [0]*n
        self.col =[0]*n
        self.diagonal = 0
        self.antidiag = 0
        self.n = n
        

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        toadd = 1 if player == 1 else -1
        
        self.row[row] += toadd
        self.col[col] += toadd
        if row == col: self.diagonal += toadd
        if col == self.n - row -1 : self.antidiag += toadd
            
        if abs(self.row[row]) == self.n or abs(self.col[col]) == self.n or abs(self.diagonal) == self.n or abs(self.antidiag) == self.n:
            return player
        else:
            return 0
        
        
        
        
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)