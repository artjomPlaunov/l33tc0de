int kthFactor(int n, int k){

    int curr = 0;
    int i = 1;
    
    for (; i*i < n; i++) {
        if (n%i == 0) 
            curr++;
        if (curr == k)
            return i;
    }
    if (i*i > n)
        i--;
    for (; i > 0; i--) {
        if (n%i == 0) {
            curr++;
        }
        if (curr == k) 
            return (n/i);
    }
    
    return -1;
}
