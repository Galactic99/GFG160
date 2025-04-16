#Reverse an array

class Solution:
    def reverseArray(self, arr):
        # code here
        left = 0
        n = len(arr)
        right = n - 1
        
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        
        return arr
            
        
        
