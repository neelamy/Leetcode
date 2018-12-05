# Source : https://leetcode.com/problems/range-sum-query-2d-immutable/description/

# Algo/DS : Array

# Complexity : O(mn)

# Explanation: https://leetcode.com/problems/range-sum-query-2d-immutable/discuss/75350/Clean-C++-Solution-and-Explaination-O(mn)-space-with-O(1)-time
'''
Construct a 2D array sums[row+1][col+1]

(notice: we add additional blank row sums[0][col+1]={0} and blank column sums[row+1][0]={0} to remove the edge case checking), so, we can have the following definition

sums[i+1][j+1] represents the sum of area from matrix[0][0] to matrix[i][j]

To calculate sums, the ideas as below

+-----+-+-------+     +--------+-----+     +-----+---------+     +-----+--------+
|     | |       |     |        |     |     |     |         |     |     |        |
|     | |       |     |        |     |     |     |         |     |     |        |
+-----+-+       |     +--------+     |     |     |         |     +-----+        |
|     | |       |  =  |              |  +  |     |         |  -  |              |
+-----+-+       |     |              |     +-----+         |     |              |
|               |     |              |     |               |     |              |
|               |     |              |     |               |     |              |
+---------------+     +--------------+     +---------------+     +--------------+

   sums[i][j]      =    sums[i-1][j]    +     sums[i][j-1]    -   sums[i-1][j-1]   +  

                        matrix[i-1][j-1]
So, we use the same idea to find the specific area's sum.

+---------------+   +--------------+   +---------------+   +--------------+   +--------------+
|               |   |         |    |   |   |           |   |         |    |   |   |          |
|   (r1,c1)     |   |         |    |   |   |           |   |         |    |   |   |          |
|   +------+    |   |         |    |   |   |           |   +---------+    |   +---+          |
|   |      |    | = |         |    | - |   |           | - |      (r1,c2) | + |   (r1,c1)    |
|   |      |    |   |         |    |   |   |           |   |              |   |              |
|   +------+    |   +---------+    |   +---+           |   |              |   |              |
|        (r2,c2)|   |       (r2,c2)|   |   (r2,c1)     |   |              |   |              |
+---------------+   +--------------+   +---------------+   +--------------+   +--------------+

'''

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        row = len(matrix)
        if row == 0: return
        col = len(matrix[0])
        self.sum = [[0 for j in range(col + 1)] for i in range(row + 1)]
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                self.sum[i][j] = self.sum[i-1][j] + self.sum[i][j-1] - self.sum[i-1][j-1] + matrix[i-1][j-1] 

        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.sum[row2 + 1][col2 + 1] - self.sum[row2 + 1][col1 ]- self.sum[row1][col2 + 1] +  self.sum[row1][col1]
            


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)