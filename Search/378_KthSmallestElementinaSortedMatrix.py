
# Source : https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

# Algo/DS : Array, Binary search

# Complexity : O(n log(max - min)) because total number = max - min so log(max-min)
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        row = len(matrix) -1
        col = len(matrix[0]) -1
        low = matrix[0][0]
        high = matrix[row][col]
        
        # do binary search
        while low <= high:
            mid = (low + high)/2
            count = self.lessthanmid(matrix, mid)
            
            # change low if count is less than k
            if count < k:
                low = mid + 1
            else:
                # change high if count > k or count = k
                high = mid - 1
        return low
    
    # find count of number less than or equal to val
    def lessthanmid(self,matrix, val):
        row = len(matrix) -1
        col = len(matrix[0]) -1
        current_row = 0
        current_col = col
        count = 0
        while current_row <= row and current_col >= 0:
            if matrix[current_row][current_col] > val:
                current_col -=1
            else:
                count += current_col + 1
                current_row += 1
        return count
        
        
        
           
        
        
        
        
        
        