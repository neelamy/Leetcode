
# Source : https://leetcode.com/problems/exclusive-time-of-functions/description/

# Algo/DS : DP, r

# Complexity : O(n)

class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        res = [0]*n
        stack = []
        
        for l in logs:
            l = l.split(":")
            id = int(l[0])
            time = int(l[-1])
            
            #append start to stack
            if l[1] == "start":
                stack.append([id, time])
            else:
            	# if its end then calculate the time
                id_end, time_start  = stack.pop()
                time_spent = time - time_start + 1

                # add it to existing value
                res[id] += time_spent
                
                # nested function time need to be deducted from the parent time, 
                # therefore update the parent function with negative children's time
                if stack: 
                    res[stack[-1][0]] -= time_spent

                    
        return res
                
                
                
            
        