# Source : https://leetcode.com/problems/wildcard-matching/description/

# Algo/DS : String, 

# Complexity : O(s+p)

# explanation : https://leetcode.com/problems/wildcard-matching/discuss/138878/Finite-state-machine-with-Python-and-dictionary.-13-lines-O(p+s)-time

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        d = {}
        state = 0

        # create finite state machine
        for char in p:
            if  char == '*': d[(state,char)] = state
            else:
                d[(state,char)] = state + 1
                state += 1
        
        # this is the final state
        final = state
        
        # put initial start state in set
        current_state = set([0])
        
        # traverse using char in s
        for element in s:
            temp = set()

            # for each element, possible set are [element, *,?]
            for char in [element ,"*", "?"]:
                # there can be many state at any given time
                for state in current_state:
                    # find the state which we will get from  (cuurent) state and char
                    # and add to the set
                    temp.add(d.get((state,char)))

            # update current state set        
            current_state = temp
       # return true if final state is reached by last element  
        return final in current_state
                    
            
        