from collections import defaultdict

class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        #Your Code goes here.
        n = len(arr)
        freq = defaultdict(int)
        result = []

        for num in arr:
            freq[num] += 1
        
        for key in freq:
            if freq[key] > n // 3:
                result.append(key)
        
        return sorted(result)
