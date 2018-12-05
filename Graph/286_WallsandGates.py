# Source : https://leetcode.com/problems/walls-and-gates/description/

# Algo/DS : Graph, BFS

# Complexity : O(nm)

class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """      
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    self.bfs(i,j, rooms,0)
                    
    def bfs(self, row, col, rooms, val):     
        queue = []
        queue.append((row, col))
        while queue:
            current_row, current_col = queue.pop(0)
            r = [-1, 0,0,1]
            c =[0,-1,1,0]
            for k in range(4):
                 if self.issafe(current_row + r[k], current_col + c[k], rooms, rooms[current_row][current_col] + 1):
                        rooms[current_row + r[k]][current_col + c[k]] = rooms[current_row][current_col] + 1
                        queue.append((current_row + r[k], current_col + c[k]))

    def issafe(self, row , col , rooms, val):
        if 0<=row<len(rooms) and 0<=col<len(rooms[0]) and  rooms[row][col] > val: 
            return True
        return False

        