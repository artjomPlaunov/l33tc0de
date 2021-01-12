int removeDuplicates(int* nums, int numsSize){
    
    if (!numsSize) {
        return 0;
    }
    
    int j = 0;
    int i = 0;
    
    while (i < numsSize-1) {
        if (nums[i] != nums[i+1]) {
            nums[j++] = nums[i];
        }
        i++;
    }
    nums[j] = nums[i];
    return j+1;
}
