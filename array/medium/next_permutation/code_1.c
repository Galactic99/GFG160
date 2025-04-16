// Function to find the next permutation
void nextPermutation(int arr[], int n) {
    // code here
    int pivot = -1;
    int left = 0;
    int right = n - 1;
    
    for(int i = n - 2; i >= 0; i--){
        if(arr[i] < arr[i + 1]){
            pivot = i;
            break;
        }
    }
    
    if(pivot == -1){
        while(left < right){
            int temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;
            left++;
            right--;
        }
        return;
    }
    
    int swapidx = pivot + 1;
    
    for(int i = pivot + 1; i < n; i++){
        if(arr[i] > arr[pivot] && arr[i] <= arr[swapidx]){
            swapidx = i;
        }
    }
    
    
    int temp = arr[pivot];
    arr[pivot] = arr[swapidx];
    arr[swapidx] = temp;
    
    int l = pivot + 1, r = n - 1;
    
    while(l < r){
        temp = arr[l];
        arr[l] = arr[r];
        arr[r] = temp;
        l++;
        r--;
    }
}