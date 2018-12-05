# Source : https://leetcode.com/problems/number-of-islands-ii/description/

# Algo/DS : Graph, Union

# Complexity : 

class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        
        # find parent if given tuple
        def get_parent(i):

            # if parent in not same then call function with its parent
            # and RESET parent of i. This eliminates need of rank
            if parent[i] != i:
                parent[i] = get_parent(parent[i])

            # return parent of i
            return parent[i]
        
        # intialization
        parent = {}
        island = set()
        result = []
        
        for i,j in positions:

            # create tuple for current position
            p = (i,j)

            # add it to parent and island
            parent[p] = p
            island.add(p)

            # check its neighbours
            for neighbour in [(i+1,j),(i-1,j),(i,j+1), (i,j-1)]:

                # if neighbour in parent then
                if neighbour in parent:

                    # get the parent
                    parent_p = get_parent(neighbour)

                    # set the parent of parent to p.i.e. current cell will be parent
                    # of all previously linked islands
                    parent[parent_p] = p

                    # if parent is not p and its in set then remove it from island set
                    # as it is no more an independent island
                    if parent_p  in island and parent_p!= p: island.remove(parent_p)
            
            # append the len of island set to result
            result.append(len(island))
        
        return result
        
           