void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n){
    int next    = m+n-1;
    int one     = m-1;
    int two     = n-1;
    
    while (one >= 0 && two >= 0) {
        if (nums1[one] > nums2[two]) 
            nums1[next--] = nums1[one--];
        else
            nums1[next--] = nums2[two--];
    }
    while (one >= 0) 
        nums1[next--] = nums1[one--];
    while (two >= 0) 
        nums1[next--] = nums2[two--];
}
