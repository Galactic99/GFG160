//This solution exceedes the time limit for large inputs. It is not correct for all d.

void rotateArr(int arr[], int n, int d) {
    // code here
    int left = 0;
    int right = n - 1;

    int starting_right = n - 1;
    int count = 0;
    int starting = d;
    
    
    int starting_left = starting;
    
    while(starting_left < starting_right){
        int temp = arr[starting_left];
        arr[starting_left] = arr[starting_right];
        arr[starting_right] = temp;
        starting_left++;
        starting_right--;
    }
    
    int left_of_starting = starting - 1;
    int right_of_starting = starting + 1;
    
    while(left_of_starting >= 0){
        int temp_1 = arr[left_of_starting];
        arr[left_of_starting] = arr[right_of_starting];
        arr[right_of_starting] = temp_1;
        left--;
        right++;
        count++;
    }
    
}