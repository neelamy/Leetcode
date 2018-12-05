# Source : https://leetcode.com/problems/word-ladder-ii/description/

# Algo/DS :  BFS, graph

# Complexity : O()

# Alternate: https://leetcode.com/problems/word-ladder-ii/discuss/40482/Python-simple-BFS-layer-by-layer


class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """

        self.d = {}
        self.create_dict(wordList)
        visited = set()
        stack = [(beginWord,1, [beginWord])]
        visited.add(beginWord)
        result = []
        min_path = float("Inf")
        while stack:
            w , step, parent = stack.pop(0)
            visited.add(w)
            if w == endWord : 
                if min_path >= step:
                    min_path = step
                    result.append(parent)
                continue

            for i in range(len(w)):
                neighbor =w[0:i] + "_" +w[i+1:]
                if neighbor in self.d:
                    for neigh in self.d[neighbor]:
                        if neigh not in visited:
                            stack.append((neigh,step + 1, parent + [neigh]))
                            
                            
        return result      
        
    def create_dict(self, wordList):
        for word in wordList:
            for i in range(len(word)):
                new_word =word[0:i] + "_" +word[i+1:]
                self.d[new_word] = self.d.get(new_word, []) + [word]
       # print self.d 
        