int maxSubarraySum(int arr[], int n) {
    // Your code here
    int maxSum = arr[0];
    int currentSum = 0;
    
    for(int i = 0; i < n; i++){
        currentSum += arr[i];
        if(currentSum > maxSum){
            maxSum = currentSum;
        }
        if(currentSum < 0){
            currentSum = 0;
        }
    }
    
    return maxSum;
}