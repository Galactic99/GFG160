def circularSubarraySum(arr):
    currMax = 0
    currMin = 0
    totalSum = 0

    max_sum = arr[0]
    min_sum = arr[0]

    for i in range(len(arr)):
        currMax = max(currMax + arr[i], arr[i])
        max_sum = max(max_sum, currMax)

        currMin = min(currMin + arr[i], arr[i])
        min_sum = min(min_sum, currMin)

        totalSum += arr[i]
    
    normalSum = max_sum
    circularSum = totalSum - min_sum

    if min_sum == totalSum:
        return normalSum

    return max(normalSum, circularSum)
