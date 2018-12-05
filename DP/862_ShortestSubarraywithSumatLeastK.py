# Source : https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/description/

# Algo/DS : Array, DP

# Complexity : O(n)

# Explanation: https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/discuss/143726/C++JavaPython-O(N)-Using-Deque?page=2
'''
Just to make things clear, the intuition behind this is, say there are indexes x and y such that x < y and
B[x] >= B[y]. Now say B[x] <= B[i] - K . This implies B[y] <= B[x] <= B[i] - K. Hence the most greedy approach 
would be to choose y instead of x, since that minimises the length of subarray.

in 1st loop we will need sum[i] - sum[q[0]] so if sum[i] - x> k then sum[i] -y will also be greater than k when x>y
we prefer y here because it will give shorter length
'''

import collections
class Solution(object):
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        n = len(A)
        sum = [0]* (n + 1)
        
        for i in range(1, n+1):
            sum[i] += sum[i-1] + A[i-1]
        #print sum
        q = collections.deque()  
        res = float("inf")
        for i in range(n + 1):
            while q and sum[i] - sum[q[0]] >= K :
                res = min(res, i - q.popleft())
            while q and sum[i] < sum[q[-1]]:
                q.pop()
            q.append(i)
        
        return res if res != float("inf") else -1
            
            