class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        #Your Code goes here.
        n = len(arr)
        req_n = n / 3
        unique_array = []
        answer_array = []
        x = 0
        
                
        for i in arr:
            if i in unique_array:
                x += 1
            else:
                current = i
                sum = 0
                for j in range(n):
                    if current == arr[j]:
                        sum += 1
                unique_array.append(current)
                if sum > req_n:
                    answer_array.append(current)
        
        answer_array.sort()
        return answer_array