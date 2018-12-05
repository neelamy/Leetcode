# Source : https://leetcode.com/problems/implement-trie-prefix-tree/description/

# Algo/DS : Trie

# Complexity : O(n) -  where n is length of word

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        
        current_node = self.root       
        for w in word:
            if w not in current_node:
                current_node[w] ={}
            current_node = current_node[w]
        current_node['#'] = 1
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current_node = self.root
        for w in word:
            if w not in current_node:
                return False
            current_node = current_node[w]
        return '#' in current_node
        
        
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current_node = self.root
        for w in prefix:
            if w not in current_node:
                return False
            current_node = current_node[w]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)