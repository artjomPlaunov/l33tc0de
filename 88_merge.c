void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n){
    int next = (n--)+(m--)-1;
    
    while (m >= 0 && n >= 0) {
        if (nums1[m] > nums2[n]) 
            nums1[next--] = nums1[m--];
        else
            nums1[next--] = nums2[n--];
    }
    while (n >= 0) {
        nums1[next--] = nums2[n--];
    }
}
