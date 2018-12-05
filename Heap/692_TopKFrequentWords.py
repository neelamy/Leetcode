# Source : https://leetcode.com/problems/top-k-frequent-words/description/

# Algo/DS : Heap

# Complexity : O(nlog k) k = no of words required, n = length of array

import heapq
from collections import Counter
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        
        d = Counter(words)           
       # return sorted(d , key = lambda x: (-d[x],x))[:k]
        heap = [(-val, key) for key,val in d.iteritems()]
        heapq.heapify(heap)       
        return [heapq.heappop(heap)[1] for i in range(k)]
        
