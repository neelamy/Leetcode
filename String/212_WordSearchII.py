# Source : https://leetcode.com/problems/word-search-ii/description/

# Algo/DS : String, Trie

# Complexity : O(n^2)

from collections import defaultdict
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        self.result = []

        # make trie
        root = Trie()
        root.maketrie(words)    
        row = len(board) 
        col = len(board[0])  

        # consider each cell as starting point     
        for i in range(row):
            for j in range(col):
                # char present in root then perform dfs 
                if board[i][j] in root.next:
                    self.dfs(i,j,board, root.next[board[i][j]])
        return self.result
                    
    
    # check is row, col is in range and char is present in node.next
    def issafe(self,i,j,board, node):
        row = len(board) -1
        col = len(board[0]) -1      
        return 0 <= i <= row and 0 <= j <= col and board[i][j] in node.next

    
    def dfs(self, i,j,board, node):       
        char = board[i][j]

        # check if this is end of word
        if  node.word != "" : 
            self.result.append(node.word)

            # do this to avoid duplicates
            node.word = ""

        r =[-1,0,0,1]
        c = [0,-1,1,0]

        # change char so that we dont need to maintain visited matrix
        board[i][j] = '#'
        
        for i1, j1 in zip(r,c):           
            if self.issafe( i + i1,j + j1,board, node):
                
                # if new char in node.next then move to that node
                self.dfs(i + i1,j + j1,board, node.next[board[i + i1][j + j1]])
        # reset char
        board[i][j] = char 
        

# create Trie       
class Trie:
    def __init__(self):
        self.next = defaultdict(Trie)
        self.word = ""
        
    def maketrie(self, words):
        for word in words:
            current = self
            for w in word:                
                current =  current.next[w]
            current.word = word
            
                