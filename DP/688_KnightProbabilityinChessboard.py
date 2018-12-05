# Source : https://leetcode.com/problems/one-edit-distance/description/

# Algo/DS : Array

# Complexity : O(N*N*K)

# explanation: https://leetcode.com/problems/knight-probability-in-chessboard/solution/

class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        
        dp_initial = [[0 for j in range(N)] for i in range(N)]
        
        row_move = [-2,-2,-1,1,2,2,-1,1]
        col_move = [-1,1,-2,-2,-1,1,2,2]
        
        dp_initial[r][c] = 1

        for k in range(K):
            dp_updated = [[0 for j in range(N)] for i in range(N)]
            for i in range(N):
                for j in range(N):
                    for s in range(8):
                        row = i + row_move[s]
                        col = j + col_move[s]
                        if 0<= row < N and 0<= col < N

                            # probability of getting to i,j in next step
                            # is sum of probability of getting to last step
                            # probability of last step = p/8 as probability
                            # of it getting selected is 8 (there are 8 poosible move for 
                            # current step)
                            dp_updated[i][j] += dp_initial[row][col]/8.0
            
            dp_initial = dp_updated

        # get the sum of all probability
        res = 0
        for i in dp_initial:
            res += sum(i)
            
        return res
            
            
            
            
            