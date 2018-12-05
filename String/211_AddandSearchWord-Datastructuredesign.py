# Source : https://leetcode.com/problems/add-and-search-word-data-structure-design/description/

# Algo/DS : Trie

# Complexity : 

from collections import defaultdict
class Trie:
    def __init__(self):
        self.next = defaultdict(Trie)
        self.isword = False
    
    def makeTrie(self, word):
        current = self
        for w in word:
            current = current.next[w]
        current.isword = True
    
    
class WordDictionary(object): 
    
    def __init__(self):
        self.root = Trie()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """   

        # make trie for new word
        self.root.makeTrie(word)
        
            
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.helper(word, self.root)
        
    def helper(self, word, node):

        # if no node then return False
        if not node: return False

        # if no chars left in word then check if its end of word in trie
        if not word: return node.isword
        
        char = word[0]

        # if char is not "." then go to next node
        if char != ".":
            if char not in node.next: return False
            return self.helper(word[1:], node.next[char])
        else:

            # else check all child node
            res =  False
            for child in node.next:
                res |= self.helper(word[1:], node.next[child])
            return res

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)