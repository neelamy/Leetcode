# Source : https://leetcode.com/problems/alien-dictionary/discuss/157298/C++-BFS-and-Topoligical-Sort-with-explanation

# Algo/DS : Topological sort, graph

# Complexity : O(n)

'''
STEP 1: Initialize
for each letter in each word degree[letter] = 0;

STEP 2: Build Graph and Record the edge
if we find a letter a != letter b in word i and i+1:
Add one to the degree of b and add letter b to letter a's set of letters, and go to the next word, 
since each word only tells us information about one pair of letters

STEP 3: Topological Sort
use queue, push all nodes which indegree is 0;
Pop letter a and append it to the res string
For each letter b in letter a's set of letters:
subtract 1 from the degree
If it's degree is 0, add it to the queue because all it's dependencies have been added already
Repeat 3
use BFS start to iterate the whole graph.

STEP 4: Tell if cyclic
compare the result with indegree if (res.size() == indegree.size());
if the size of the result string != the size of the initialized letters then return an empty
string(not all of the degrees hit 0 so there's a conflict)
'''

class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        letter = set()
        degree = {}
        graph = {}

        # find all letters
        for word in words:
            for w in word:
                letter.add(w)
        
        # initialize       
        for char in letter:
            degree[char] = 0
            graph[char] = set()   

        # build graph and record indegree
        for i in range(len(words)-1):
            # compare word only with next word
            j = i + 1
            for k in range(len(words[i])):
                if len(words[j]) > k and words[i][k] != words[j][k] :

                    # increment degree only if its not already added
                    # eg there might be words like ac, ab, vc,vb so c--> b must be
                    # added just once
                    if words[j][k] not in graph[words[i][k]]:
                        graph[words[i][k]].add(words[j][k])
                        degree[words[j][k]] += 1
                    # break whenever diff found even if degree count isnt incremented
                    break
                        
        result = ""
        
        stack = []
        
        # add all nodes with 0 degree
        for i in degree:
             if degree[i] == 0: stack.append(i)
        
        # do topological sort using bfs
        # DFS wont work due to cycle.
        while stack:    

            # pop from stack and add to result     
            current = stack.pop(0)
            result += current

            # traverse its neighbours and reduce their degree by 1
            # if degree is 0 then add to stack
            for i in graph[current]:
                degree[i]-= 1
                if degree[i] == 0: stack.append(i)
        
        #  check if all letters are there in result else there was cycle 
        return result if len(result) == len(letter) else ""



