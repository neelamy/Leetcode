# Source : https://leetcode.com/problems/the-skyline-problem/description/

# Algo/DS : Heap, skyline

# Complexity : O(nlog ) 


from heapq import heappush, heappop

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        
        # store points with -h for start end h for end
        # reason: helps in sortinf
        #1.if 2 ponits are same and are start so consider largest height first
        #2.if 2 ponits are same and are end so consider smallest height first
        #3.if 2 ponits are same and are start and end so consider start first
        points = []
        for i in range(len(buildings)):
            x,y,h = buildings[i]
            points.append([x, -h])
            points.append([y, h])
            
        points.sort()

        # create priority queue
        pq = []
        result = []

        # push 0
        heappush(pq, 0)
        prev_max = 0

        # this will store all heighsof end points that needs to be removed
        end_height = {}

        # traverse all points
        for x, h in points:

            # if its start then just add to pq
            if h < 0:
                heappush(pq, h)
            
            # else add to end_height. Increament count to keep track of duplicates   
            else:
                end_height[-h] = end_height.get(-h, 0) + 1

            # Remove heights if they become the root of the heap and are in end_heights
            while pq[0] in end_height and end_height[pq[0]] > 0:
                end_height[pq[0]] -=1
                heappop(pq)
            
            # if previous max changes then add it to result                           
            current_max = abs(pq[0])       
            if prev_max != current_max:
                result.append([x,current_max] )
                prev_max = current_max
                
                
        return result