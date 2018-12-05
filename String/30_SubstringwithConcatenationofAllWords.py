# Source : https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/

# Algo/DS : string, word combination

# Complexity : O(nk)



from collections import Counter

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words: return []
        
        # get words and their freq
        d = Counter(words)

        # total words
        total_words = len(words)

        # length of each word
        word_length = len(words[0])
        result = []

        # length that we need to check
        expected_length = total_words*word_length 

        # i goes from 0 to len(s) - expected_length + 1
        for i in range(0, len(s) - expected_length + 1) :

            # create copy of d for each i
            temp_d = dict(d)
            word_count = 0

            # check words starting from j
            for j in range(i, i + expected_length, word_length):
                currnt_word = s[j: j + word_length]

                # if word in dict then reduce freq by 1 and inc word_count
                if currnt_word in temp_d and temp_d[currnt_word] > 0:
                    temp_d[currnt_word] -=1
                    word_count += 1
                else:
                    # else break
                    break

            # if all words seen then add i
            if word_count == total_words: 
                result.append(i)
                
        return result
   