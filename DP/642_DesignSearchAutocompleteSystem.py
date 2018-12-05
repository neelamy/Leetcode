# Source : https://leetcode.com/problems/design-search-autocomplete-system/description/

# Algo/DS : Trie, DP

# Complexity : 


from collections import defaultdict

class AutocompleteSystem(object):

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.current_input = ""
        
        self.freq = defaultdict(int)
        self.prefix = defaultdict(list)     
        for sentence, time in zip(sentences, times ):
            self.addWord(sentence, time)
            
    def addWord(self, sentence, time):
        # if sentence is already in freq then do not create its prefix
        if sentence not in self.freq :       
            for i in range(1, len(sentence) + 1):
                self.prefix[sentence[:i]].append(sentence)
        self.freq[sentence] += time
          
        
    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        if c == "#":
            self.addWord(self.current_input, 1)
            self.current_input = ""
            return []
        self.current_input += c
        if self.current_input in self.prefix:
            result = self.prefix[self.current_input]
            result.sort(key = lambda x:(-self.freq[x], x))
            return result[:3]
        
        return []

   
# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
