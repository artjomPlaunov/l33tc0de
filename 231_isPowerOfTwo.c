bool isPowerOfTwo(int n){
    if (!n) 
        return false;
    
    int mask = 1;
    int count = 0;
    while (n) {
        if (n & 1) {
            count += 1;
            if (count > 1) 
                return false;
        }
        n = n >> 1;
    }
    return true;
}
