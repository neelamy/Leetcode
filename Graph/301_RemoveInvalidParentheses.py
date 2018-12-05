
# Source : https://leetcode.com/problems/remove-invalid-parentheses/description/

# Algo/DS : BFS

# Complexity : O(n * (2^n)): n to check if parantheses is valid 2^n as each element can 
# be either added or removed

# Explaination : https://leetcode.com/problems/remove-invalid-parentheses/discuss/75041/Java-BFS-solution-16ms-avoid-generating-duplicate-strings
# https://leetcode.com/problems/remove-invalid-parentheses/discuss/75027/Easy-Short-Concise-and-Fast-Java-DFS-3-ms-solution


class Parentheses:
        def __init__(self, s, index, char):
            self.string = s
            self.last_index = index
            self.removed_char = char

class Solution(object):
    def isvalid(self, s):
        #print s
        count = 0
        for i in s:
            if i =='(' : count += 1
            elif i ==')' : count -= 1 
            if count < 0: return False
        return count == 0
    
    
        
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []    

        # check if already valid    
        if self.isvalid(s): return [s]
        queue = []

        # else add to queue and start BFS
        queue.append(Parentheses(s,0,')'))
        while queue:

            # get the 1st item from queue
            item = queue.pop(0)
            
            st = item.string
            
            # start traversing it from last_index position
            for i in range(item.last_index, len(st)):

                # skip it is same as last char
                if i != item.last_index and st[i-1] == st[i]: continue

                # skip if its not ( or )
                if st[i] not in ['(', ')']: continue

                # skip if last removed was ( and this item is ) as they form valid pair
                # so string with them will be valid with less parentheses removed
                if item.removed_char == '(' and st[i] == ')': continue
                
                # remove char at ith index
                new_string = st[0:i]+ st[i+1:]

                # if its valid then add to result 
                if self.isvalid(new_string):
                    res.append(new_string)
                else:

                    # add to queue only when res is empty so that smaller length valid strings are not added
                    # else for ())(), string like () will be added to result
                    if not res:
                        queue.append(Parentheses(new_string,i,st[i] ))
        
        
        return res


'''

class Solution {
    public List<String> removeInvalidParentheses(String s) {
        List<String> output = new ArrayList<>();
        removeHelper(s, output, 0, 0, '(', ')');
        return output;
    }

    public void removeHelper(String s, List<String> output, int iStart, int jStart, char openParen, char closedParen) {
        int numOpenParen = 0, numClosedParen = 0;
        for (int i = iStart; i < s.length(); i++) {
            if (s.charAt(i) == openParen) numOpenParen++;
            if (s.charAt(i) == closedParen) numClosedParen++;
            if (numClosedParen > numOpenParen) { // We have an extra closed paren we need to remove
                for (int j = jStart; j <= i; j++) // Try removing one at each position, skipping duplicates
                    if (s.charAt(j) == closedParen && (j == jStart || s.charAt(j - 1) != closedParen))
                    // Recursion: iStart = i since we now have valid # closed parenthesis thru i. jStart = j prevents duplicates
                        removeHelper(s.substring(0, j) + s.substring(j + 1, s.length()), output, i, j, openParen, closedParen);
                return; // Stop here. The recursive calls handle the rest of the string.
            }
        }
        // No invalid closed parenthesis detected. Now check opposite direction, or reverse back to original direction.
        String reversed = new StringBuilder(s).reverse().toString();
        if (openParen == '(')
            removeHelper(reversed, output, 0, 0, ')','(');
        else
            output.add(reversed);
    }
}'''
        
      
    