# Source : https://leetcode.com/problems/palindrome-pairs/description/

# Algo/DS : Trie

# Complexity : 



from collections import defaultdict

# this function will return True if word is palindrome
def ispalindrome(word):
	return word == word[::-1]

class Trie(object):

	# each trie element will have trie dictionary, isEnd to mark end of branch and 
	# palindrome to store index of word below this node which are palindrome
	def __init__(self):
		self.trie = defaultdict(Trie)
		self.isEnd = None
		self.palindrome = [] 

	# this will create trie by adding words in reverse order
	def makeTrie(self, words):
		for index, word in enumerate(words):
			current_node = self
			word = word[::-1]
			for ind, char in enumerate(word):
				current_node = current_node.trie[char]

				# if remaining chars form palindrome then save the index in this nodes's palindrome list
				if word[ind + 1:] and ispalindrome(word[ind + 1:]): current_node.palindrome.append(index)			   
			# mark the end of word by storing its index in isEnd
			current_node.isEnd = index


class Solution(object):

	def palindromePairs(self, words):
		"""
		:type words: List[str]
		:rtype: List[List[int]]
		"""

		#create trie with inverted word
		# store index at the end
		# for each char, store index if remaining chars form palindrome
		root = Trie()
		root.makeTrie(words)

		
		result = []
		# now check for each word if they exist in trie
		for index, word in enumerate(words):
			temp = []
			brk = False
			current_node = root
			for ind, char in enumerate(word):

				# char is not in dict then break and do not process remaining things
			 	if char not in current_node.trie: 
			 		brk = True
			 		break

			 	# move down the dict
			 	current_node = current_node.trie[char]
				
				# if trie branch is smaller than word, check if remaining char in word form palindrome
				# if yes, then store index of current branch as it is of form ac___ca. where __ are
				# palindrome created by extra chars of word
				if current_node.isEnd != None :  
					if word[ind + 1:] and  ispalindrome(word[ind + 1:]): temp.append(current_node.isEnd)

							
			
			if not brk:
				# if trie branch and word have same length
			  	if current_node.isEnd != None : temp.append(current_node.isEnd )

			  	# if trie branch is larger than word, add palindrome list as it contains list
			  	# of all words which forms palindrome after this point
			  	if current_node.palindrome: temp.extend(current_node.palindrome)

			# add value from temp if they are not same as current index
			result += [ [index,i] for i in temp if i != index]

			if word == "":
				result += [ [index,ind] for ind, word in enumerate(words) if self.ispalindrome(word) and ind != index] 
				result += [ [ind,index] for ind, word in enumerate(words) if self.ispalindrome(word) and ind != index]			
		return result

#words = ["abcd","dcba","lls","s","sssll"]   
words = ["a","b","c","ab","ac","aa"]		 
print Solution().palindromePairs(words)			   
				
			
				
		
				
