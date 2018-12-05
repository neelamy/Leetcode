# Source : https://leetcode.com/problems/word-ladder/description/

# Algo/DS : BFS

# Complexity : 

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        self.d = {}
        self.create_dict(wordList)
        visited = set()
        stack = [(beginWord, 1)]
        visited.add(beginWord)
        
        # perform bfs
        while stack:
            w , step = stack.pop(0)
            if w == endWord : return step         
            for i in range(len(w)):
                neighbor =w[0:i] + "_" +w[i+1:]
                if neighbor in self.d:
                    for neigh in self.d[neighbor]:
                        if neigh not in visited:
                            stack.append((neigh, step + 1))
                            visited.add(neigh)
                            
        
        return 0
            
        
    # create list of neighbours like for dog it would be _og,do_,do_   
    def create_dict(self, wordList):
        for word in wordList:
            for i in range(len(word)):
                new_word =word[0:i] + "_" +word[i+1:]
                self.d[new_word] = self.d.get(new_word, []) + [word]

        