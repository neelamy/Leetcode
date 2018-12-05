import random
from collections import defaultdict
class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = defaultdict(set)
        self.item = []
        
    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """

        # always add number to list as it will be used to random.choice to get random no
        # based on occuranceof number
        self.item.append(val)

        # in dictionary, add the index of number in the array in set
        # we use set as we need to remove indexes randomly later so dont use list
        if val in self.d:
            self.d[val].add(len(self.item) - 1)
            return False
        self.d[val].add(len(self.item) - 1)
        return True
        

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """

        # if val not present : return False
        if val not in self.d: return False

        # get the index where val is present. val will be removed from here so we need to pop 
        # index value from dictionary
        index_to_be_removed = self.d[val].pop()

        # del from dict if set is empty
        if len(self.d[val]) == 0: del self.d[val]
        
        # if index is not index then we need to swap last numer with the val
        # update dict accordingly and then pop last element from array  
        if index_to_be_removed != len(self.item) - 1:

            # get the last item
            last_item =  self.item[-1]

            # last number was present as len(arrry) - 1 loc so remove that location
            # and add the index of val
            self.d[last_item].remove(len(self.item) - 1)
            self.d[last_item].add(index_to_be_removed)

            # copy last item to new location in array
            self.item[index_to_be_removed]= last_item
            
        # remove last item   
        self.item.pop() 
        
        return True
        

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """

        # choice will return random number from the given list
        return random.choice(self.item)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()