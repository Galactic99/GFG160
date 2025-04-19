int max(int a, int b){
    return a > b ? a : b;
}

int min(int a, int b){
    return a < b? a : b;
}

// Function to find maximum product subarray
int maxProduct(int arr[], int n) {
    // code here...
    int max_current = arr[0];
    int min_current = arr[0];
    int req_max = arr[0];
    
    for(int i = 1; i < n; i++){
        int temp = max_current;
        
        max_current = max(arr[i], max(arr[i] * max_current, arr[i] * min_current));
        min_current = min(arr[i], min(arr[i] * temp, arr[i] * min_current));
        
        req_max = max(req_max, max_current);
    }
    
    return req_max;
}