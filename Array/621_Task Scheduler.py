# Source : https://leetcode.com/problems/task-scheduler/description/

# Algo/DS : Array

# Complexity : O(n) for traversing tasks once. For sorting frey, its (26log26) = O(1),
# then traversing freq again is O(26) = O(1)

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if not tasks : return 0      
        if n== 0 : return len(tasks)
        freq =[0] * 26
        
        # get frequncy count of each task
        for char in tasks:
            freq[ord(char) - ord('A')] += 1 

        # get the max freq
        freq = sorted(freq)
        max_freq = freq[-1]

        # idle slots = (max_freq - 1)* n as no free slot required for last item 
        idle_slot = (max_freq - 1) * n
        
        # for other, if their freq is less than max_freq, reduce idel slot by their freq
        # if freq is same as max_freq then reduce freq -1 as only it can use idle space only freq-1 times
        # [A,A,A,B,B,B]: A_ _ A _ _ A. Idle slot = 4. But B can use only 2 as remaning B will be ob right slide of
        # last A ,AB _ A B _ AB
        for count in freq[0:len(freq) - 1]:
            idle_slot -= count if count != max_freq else count - 1

        # idle_slot can go to negative so add only if its +ve
        return idle_slot + len(tasks) if idle_slot > 0 else len(tasks)
        
            
        
        