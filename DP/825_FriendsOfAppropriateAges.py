
# Source : https://leetcode.com/problems/friends-of-appropriate-ages/description/

# Algo/DS : Array, DP

# Complexity : O(121 + N)

class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        
        # get total number of people for each age
        agecount = [0]*121       
        for i in ages:
            agecount[i] += 1
        
        # get cummulative count for age    
        commulative_count = [0]* 121
        for i in range(121):
            commulative_count[i] = commulative_count[i-1] + agecount[i]
            
        res= 0

        # start age from 15 as for i< 15, i/2+ 7 will be greater than i and then
        # they cant be friend
        for i in range(15, 121):
            if agecount[i] > 0:
                
                # eligible people = total people of age i - total people of age i/2+2               
                eligible_friend = commulative_count[i] - commulative_count[(i/2) + 7]

                # res += (eligible ppl) * count of ppl of age i -(count of ppl of age i) as they 
                # cant be friend with themselves 
                res += eligible_friend* agecount[i] - agecount[i]
            
        return res
        
        
        
        