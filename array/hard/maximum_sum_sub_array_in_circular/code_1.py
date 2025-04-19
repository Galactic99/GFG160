def circularSubarraySum(arr):
    n = len(arr)

    suffixSum = arr[n - 1]

    maxSuffix = [0] * (n + 1)
    maxSuffix[n - 1] = arr[n - 1]

    for i in range(n - 2, -1, -1):
        suffixSum += arr[i]
        maxSuffix[i] = max(maxSuffix[i + 1], suffixSum)

    circularSum = arr[0]

    normalSum = arr[0]

    currSum = 0
    prefix = 0
    
    for i in range(n):
        currSum += max(currSum + arr[i], arr[i])
        normalSum = max(normalSum, currSum)

        prefix += arr[i]
        circularSum = max(circularSum, prefix + maxSuffix[i + 1])

    return max(normalSum, circularSum)