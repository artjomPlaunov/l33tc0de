

void swap(int *nums, int lo, int hi) {
    int tmp = nums[lo];
    nums[lo] = nums[hi];
    nums[hi] = tmp;
}

int partition(int* nums, int lo, int hi) {
    int pivot = nums[hi];
    int next = lo;
    for (int i = lo; i <= hi; i++) {
        if (nums[i] < pivot) {
            swap(nums, next, i);
            next += 1;
        }
    }
    swap(nums, next, hi);
    return next;
}

int aux(int* nums, int lo, int hi, int k) {
    if (lo == hi) {
        return nums[lo];
    }
    int p = partition(nums, lo, hi);
    if ( (hi-p+1) == k) {
        return nums[p];
    } else if ( (hi-p+1) > k ) {
        return aux(nums, p+1, hi, k);
    } else {
        return aux(nums, lo, p-1, k-(hi-p+1));
    }
}


int findKthLargest(int* nums, int numsSize, int k){
    return aux(nums, 0, numsSize-1, k);
}
