# Source : https://leetcode.com/problems/valid-palindrome/description/

# Algo/DS : string, palindrome

# Complexity : O(nlogn)
# explanation:https://leetcode.com/problems/next-closest-time/discuss/163539/Beat-100:-Efficient-(Python)-Solution-with-Detailed-Explanation

class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        res = [0]*4
        
        # inverse the array so that we process least sign bit first
        nums = [ int(i) for i in time if i != ':'][::-1]
        
        # arrange unique number in ascending order
        digits = sorted(list(set(nums)))
        
        # this will be limit of each index
        limits = [9,5,9,2]
        
        # if last number ie. hour starts with 2 then its next number will have limit 3
        # we do this because, if we reach limits[2] that means minutes digits are greater
        #than hour so smallest digits are in hour. first digit can be 0,1,2 and second can be anything
        # we then have to check if first digit is 2 then we have to set 3 as limit for 2nd digit of hour
        if nums[-1] == 2: limits[2] = 3
            
        for index, n in enumerate(nums):
            
            # find if next bigger index present for n
            # i.e. number greater than n present
            next = digits.index(n) + 1
            
            # check if that number is within limit for that index
            if next < len(digits)  and digits[next]<=limits[index]:
                
                # if yes, we found the next smallest number so quit
                res[index] = digits[next]
                break
                
            else:
                # else assign smallest number to that index
                res[index] = digits[0]
                
        # append remaing number to res
        for i in range(index +1, len(nums)):
            res[i] = nums[i]
            
        # convert to string and add :
        res = map(str,res[::-1] ) 
        res = "".join(res)
        return res[:2]+ ":" + res[2:]
                
                
        