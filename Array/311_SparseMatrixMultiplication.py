# Source : https://leetcode.com/problems/sparse-matrix-multiplication/description/

# Algo/DS : Matrix multiplication

# Complexity : O(n^3)

# explanation : https://leetcode.com/problems/sparse-matrix-multiplication/discuss/76151/54ms-Detailed-Summary-of-Easiest-JAVA-solutions-Beating-99.9

class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        C =[[0 for _ in range(len(B[0]))] for _ in range(len(A))]
        
        # just put k before j and check if A[i][k] is 0
        for i in range(len(A)):            
            for k in range(len(B)):
                if A[i][k] == 0 : continue
                for j in range(len(B[0])):
                    C[i][j] += A[i][k] * B[k][j]
        return C
                           
 