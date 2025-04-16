#Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        high = low = -1
        
        for i in arr:
            if i > high:
                low = high
                high = i
            elif high > i > low:
                low = i
        if low == -1:
            return -1
        else:
            return low
            
