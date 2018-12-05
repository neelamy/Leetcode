# Source : https://leetcode.com/problems/permutations-ii/description/

# Algo/DS : Array

# Complexity : O(n^3) 



   
def permuteUnique(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    result = [[]]
    
    for index, number in enumerate(nums):
        temp = []
        for current in result:
            for pos in range(len(current) + 1):
                temp.append(current[:pos] + [number] + current[pos:])

                # this is to eliminate duplicates
                # break as other cases will be covered in other lists
                if pos < index and current[pos] ==  number :break
        result = temp
        
    return result
