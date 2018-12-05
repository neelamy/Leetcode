
# Source : https://leetcode.com/problems/two-sum-iii-data-structure-design/description/

# Algo/DS : DP, stack

# Complexity : O(n)

class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        self.d[number] = self.d.get(number, 0) + 1
        

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        
        for i in self.d:
            if value - i in self.d :
                if i == value - i and self.d[value - i] > 1: return True
                elif i != value - i : return True
        
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)