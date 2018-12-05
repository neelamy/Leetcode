# Source : https://leetcode.com/problems/reverse-pairs/description/

# Algo/DS : Merge Sort, inversion

# Complexity : O(nlog n) 

# Explanation: https://leetcode.com/problems/reverse-pairs/solution/


class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        return self.mergesort(nums, 0, len(nums)-1)
    
    # perform merge sort
    def mergesort(self, nums, low, high):
        if low >= high : return 0
        mid = (low + high)/2
        
        # get count for left array and right array
        count = self.mergesort(nums, low, mid) + self.mergesort(nums, mid+1, high)
        j = mid+1

        # get count for combine left and right array
        # second array is sorted and starts from mid +1
        # check for each i , how many elements in second array is smaller
        # no need to reset j everytime as first array is also sorted so
        # number is less than a[i] then it will also be less than a[i+1]
        for i in range(low,mid+1):
            while j <= high and nums[i] > 2*nums[j]: j+=1
            count += j-(mid+1)
        
        # merge array   
        self.merge(nums, low, mid, high)
        return count
    
    # merge left and right array in place
    def merge(self,nums, low, mid, high):
        n1 =  mid-low+1
        n2= high-mid
        
        L1 = [ nums[i] for i in range(low, mid+1)]
        L2 = [ nums[i] for i in range(mid+1, high+1)]
        k = low
        i = 0
        j = 0
        while i < n1 and j < n2:
            #print i, j, L1, L2
            if L1[i] <= L2[j]:
                nums[k] = L1[i]
                i += 1
            else:
                nums[k] = L2[j]
                j += 1
            k += 1
            
        while i < n1:
            nums[k] = L1[i]
            i += 1
            k += 1
            
        while j < n2:
            nums[k] = L2[j]
            j += 1
            k += 1
   