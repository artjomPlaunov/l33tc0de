void moveZeroes(int* nums, int numsSize){
    int next = 0;
    while (next < numsSize && nums[next] != 0) {
        next++;
    }
    int ptr = next+1;
    while (ptr < numsSize) {
        if (nums[ptr] != 0) {
            nums[next] = nums[ptr];
            nums[ptr] = 0;
            next++;
        }
        ptr++;
    }
}
