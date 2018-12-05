
# Source : https://leetcode.com/problems/word-search/description/

# Algo/DS : Graph, DFS

# Complexity : O(n^2 * 3^k) k = length of word
'''
I conclude the runtime is O(n^2 * 4 * 3^(k-1)) = O(n^2 * 3^k).
Explanation: We start the word search over all n^2 nodes. For the first letter of 
the word search we can move in 4 directions but for every later one there are only three options 
(you can't move back onto yourself).
'''
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        row = len(board) 
        col = len(board[0]) 
        visited =[[False for j in range(col)] for i in range(row)]        
        for i in range(row):
            for j in range(col):
                if not visited[i][j] and board[i][j] == word[0]:
                    print i, j, word[0]
                    if self.dfs(i,j,board, visited,word[1:]): return True
        return False
                    
    
    
    def issafe(self,i,j,board, visited, char):
        row = len(board) -1
        col = len(board[0]) -1      
        return 0 <= i <= row and 0 <= j <= col and not visited[i][j] and board[i][j] == char
    
    def dfs(self, i,j,board, visited,word):
        if  word == "" : return True
        visited[i][j] = True     
        r =[-1,0,0,1]
        c = [0,-1,1,0]
        
        for i1, j1 in zip(r,c):
            if self.issafe( i + i1,j + j1,board, visited, word[0]):
                if self.dfs(i + i1,j + j1,board, visited,word[1:]): return True
        visited[i][j] = False 
            
                