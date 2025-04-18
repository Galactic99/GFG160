class Solution:
    def getMinDiff(self, arr,k):
        # code here
        arr.sort()
        
        ans = arr[-1] - arr[0]
        
        for i in range(1, len(arr)):
            if arr[i] - k < 0:
                continue
            
            minElem = min(arr[0] + k, arr[i] - k)
            maxElem = max(arr[i - 1] + k, arr[-1] - k)
            
            ans = min(ans, maxElem - minElem)
        
        return ans